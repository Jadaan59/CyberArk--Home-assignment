import argparse
import subprocess
import re
import os

CHUNK_SIZE = 300
OVERLAP = 20

def read_file_lines(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.readlines()

def chunk_lines(lines):
    for i in range(0, len(lines), CHUNK_SIZE - OVERLAP):
        yield i, lines[i:i + CHUNK_SIZE]

def build_prompt(chunk, with_fix=False):
    instructions = "You are a security analysis expert. You analyze C/C++ source code and identify potential vulnerabilities."
    if with_fix:
        instructions += " For each issue, also suggest a one-line fix if possible."
    instructions += " Respond only in this format: Line <number>: <description>. [Optional Fix: <fix>]"
    code = "".join(chunk)
    return f"{instructions}\n\n{code}"

def query_llm(prompt, chunk_index):
    print(f"\n🧠 [Chunk {chunk_index}] Sending prompt to LLM...")
    try:
        result = subprocess.run(
            ["ollama", "run", "gemma3:1b"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=180  # prevent hanging forever
        )
        stderr = result.stderr.decode()
        if stderr:
            print(f"⚠️ Ollama stderr:\n{stderr}")
        output = result.stdout.decode()
        print(f"✅ LLM response received (Chunk {chunk_index})")
        print(f"--- Raw Output ---\n{output[:500]}...\n")  # Print first 500 chars
        return output
    except subprocess.TimeoutExpired:
        print(f"⏱️ Timeout: LLM took too long on chunk {chunk_index}")
        return ""

def parse_output(output):
    findings = []
    pattern = re.compile(r"Line (\d+): (.*?)(?:\. \[Optional Fix: (.*?)\])?")
    for match in pattern.finditer(output):
        line, desc, fix = match.groups()
        findings.append((int(line), desc.strip(), fix.strip() if fix else None))
    return findings

def analyze_file(filepath, with_fix=False):
    lines = read_file_lines(filepath)
    all_findings = []

    for i, (start_idx, chunk) in enumerate(chunk_lines(lines), start=1):
        prompt = build_prompt(chunk, with_fix)
        output = query_llm(prompt, i)
        findings = parse_output(output)
        if not findings:
            print(f"⚠️ No findings detected in Chunk {i}. Possibly unrecognized format.")
        all_findings.extend(findings)

    return sorted(all_findings, key=lambda x: x[0])

def print_findings(findings, with_fix=False):
    if not findings:
        print("✅ No vulnerabilities found.")
        return

    print("\n🔒 Detected Vulnerabilities:")
    for line, desc, fix in findings:
        print(f"Line {line}: {desc}.")
        if with_fix and fix:
            print(f"  Suggested Fix: {fix}")

def main():
    parser = argparse.ArgumentParser(description="LLM-based C/C++ vulnerability analyzer")
    parser.add_argument("source_file", help="C/C++ source file to analyze")
    parser.add_argument("--fix", action="store_true", help="Suggest fixes for vulnerabilities")
    parser.add_argument("--output", default="vuln_report.txt", help="Output file for results")
    args = parser.parse_args()

    print(f"📄 Analyzing: {args.source_file}")
    if not os.path.exists(args.source_file):
        print(f"❌ File not found: {args.source_file}")
        return

    findings = analyze_file(args.source_file, with_fix=args.fix)

    with open(args.output, "w") as f:
        if not findings:
            f.write("✅ No vulnerabilities found.\n")
        else:
            for line, desc, fix in findings:
                f.write(f"Line {line}: {desc}.\n")
                if args.fix and fix:
                    f.write(f"  Suggested Fix: {fix}\n")

    print(f"✅ Analysis complete. Report saved to {args.output}")

if __name__ == "__main__":
    print("🚀 Analyzer started")
    main()
