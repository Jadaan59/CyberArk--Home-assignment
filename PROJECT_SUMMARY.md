# Project Summary – CLI Vulnerability Analyzer

## Objective
Build a command-line tool that analyzes C/C++ code for vulnerabilities using a local language model (LLM) running completely offline inside Docker.

## Initial Approach
We first attempted to implement the tool using Python and `llama-cpp-python`. However, due to:
- macOS restrictions on system Python (`PEP 668`),
- Compatibility issues on ARM and other systems,
we decided to move away from Python for this task.

## Final Setup
We used `llama.cpp` directly within a Docker container:
- Built `llama-cli` from source.
- Copied the model and analysis script into the image.
- Ensured everything runs locally and identically across environments.

## Model Choice
We selected `gemma-2b-it.Q4_K_M.gguf`:
- Small size (~1.5 GB), ideal for CPU-only inference.
- Instruction-tuned and compatible with `llama.cpp`.
- Fully offline execution using the GGUF format.

## Token Limit Handling
LLMs like Gemma have a 4096-token limit. Full C files often exceed this.

**Solution**: We split the input file into logical blocks (e.g., functions) and analyze them one at a time. Each block is sent as a separate prompt.

## Project Structure
```
CyberArk--Home-assignment/
├── Dockerfile
├── model/                  ← Contains the GGUF model
├── src/analyze.sh          ← Main script to analyze code blocks
├── library.c               ← Sample test file
├── README.md
```