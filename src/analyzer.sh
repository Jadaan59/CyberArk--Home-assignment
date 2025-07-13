#!/bin/bash

# Path to the local GGUF model file
MODEL_PATH="/app/model/gemma-2b-it.Q4_K_M.gguf"

# Get the input C file from command-line arguments
INPUT_FILE=$1

# Check if the user provided a file
if [ -z "$INPUT_FILE" ]; then
  echo "❌ Error: no input file provided."
  echo "Usage: $0 <c_file>"
  exit 1
fi

# Initialize variables
BLOCK=""          # Stores current code block
IN_BLOCK=0        # Flag to indicate if we're inside a block
BRACE_COUNT=0     # Tracks the number of open/closed braces
BLOCK_NUM=1       # For labeling each block

# Read the input file line-by-line
while IFS= read -r LINE || [[ -n "$LINE" ]]; do

  # If we're not inside a block, look for a new one starting (line ends with '{')
  if [[ "$IN_BLOCK" -eq 0 && "$LINE" =~ \{$ ]]; then
    IN_BLOCK=1
    BRACE_COUNT=1
    BLOCK="$LINE"$'\n'

  # If we are inside a block, keep appending lines to it
  elif [[ "$IN_BLOCK" -eq 1 ]]; then
    BLOCK+="$LINE"$'\n'

    # Update brace count:
    # +1 for each '{', -1 for each '}'
    BRACE_COUNT=$(( BRACE_COUNT + $(grep -o '{' <<< "$LINE" | wc -l) - $(grep -o '}' <<< "$LINE" | wc -l) ))

    # If brace count is back to zero — the block has ended
    if [[ "$BRACE_COUNT" -le 0 ]]; then
      echo "🔍 Analyzing block #$BLOCK_NUM..."

      # Create the prompt for LLM
      PROMPT="You are a security expert. Analyze the following C code block and list any vulnerabilities with line numbers and explanations:\n\n\`\`\`c\n$BLOCK\n\`\`\`"

      # Run the model on this block
      llama-cli --model "$MODEL_PATH" -p "$PROMPT"

      echo "------------------------------------------------------------"

      # Reset block-related variables
      IN_BLOCK=0
      BLOCK=""
      BLOCK_NUM=$((BLOCK_NUM + 1))
    fi
  fi
done < "$INPUT_FILE"


