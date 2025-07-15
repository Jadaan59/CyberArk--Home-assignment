import ollama
import os
import sys

CHUNK_SIZE = 150  # lines per chunk, modify as needed

def chunk_code(code, size=CHUNK_SIZE):
    """

    :param code: the source code
    :param size: default is CHUNK_SIZE
    :return: generates the chunk code
    """
    lines = code.splitlines()
    for i in range(0, len(lines), size):
        yield i + 1, "\n".join(lines[i:i + size])

def build_prompt(chunk, start_line):
    """

    :param chunk: the chunck code
    :param start_line: base line start the chunck
    :return: the prompt for the chunck
    """
    return f""" 
You are a security expert. Analyze the following C/C++ code (starting at line {start_line}) for vulnerabilities.

For each issue you find, use this format:

‼️ Vulnerability detected at line X (make sure the line is good) :
Code: `...`
Issue: ...
Suggested Fix: ...

Here is the code to analyze:
------------------------------
{chunk}
------------------------------

Remember to write short answers, dont write unnecessarily lines.
"""

def main():
    print("📁 analyzer.py running...")
    file_to_analyze = sys.argv[1] if len(sys.argv) > 1 else None
    print(f"📂 File to analyze: {file_to_analyze}")

    if not file_to_analyze or not os.path.exists(file_to_analyze):
        print("❌ File not provided or not found.")
        return

    with open(file_to_analyze, 'r') as f:
        code = f.read()

    client = ollama.Client() #open a client server API call
    model = "gemma3:4b" #change as needed

    for start_line, chunk in chunk_code(code):
        prompt = build_prompt(chunk, start_line)
        try:
            print(f"\n🔎 Analyzing lines {start_line}–{start_line + CHUNK_SIZE - 1}...")
            response = client.generate(model=model, prompt=prompt)
            output = response['response'] if isinstance(response, dict) else response.response
            print(output)
        except Exception as e:
            print(f"❌ Failed analyzing chunk starting at line {start_line}: {e}")

if __name__ == "__main__":
    main()
