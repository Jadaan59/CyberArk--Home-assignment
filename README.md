# 🔍 C/C++ Vulnerability Analyzer (LLM-Powered)

This CLI tool detects security vulnerabilities in C/C++ source files using a locally running large language model (LLM) via [Ollama](https://ollama.com). It reads your code, chunks it intelligently, and asks the model to identify potential security flaws — all running offline on your machine.

---

## ✨ Features

- 🔐 Analyzes C/C++ files for common security issues
- 📦 Works fully offline with local LLMs (e.g., `gemma3:4b`)
- 📚 Processes large files in chunks for more stable results
- ✅ Simple CLI interface with clean output
- 💬 Uses structured prompts for consistent and accurate answers

---

## 📦 Requirements

- Python 3.8 or newer
- [Ollama](https://ollama.com) installed on your machine
- An Ollama-compatible model (e.g., `gemma3:4b`) downloaded locally

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/c-analyzer.git
cd c-analyzer
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install ollama
```

### 4. Install Ollama

Follow instructions from [ollama.com/download](https://ollama.com/download) or use:

#### macOS (via Homebrew)
```bash
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Windows
Use the [official installer](https://ollama.com/download)

---

### 5. Download a Model (e.g., Gemma 4B)

```bash
ollama pull gemma3:4b
```

Make sure the model download finishes completely before continuing.

---

### 6. Start the Ollama Server

Open a separate terminal and run:

```bash
ollama serve
```

Leave this running in the background — it acts as a local API server.

---

### 7. Run the Analyzer

In your main terminal (with the virtual environment activated):

```bash
python analyzer.py path/to/your/code.c
```

Example:

```bash
python analyzer.py library.c
```

---

## 🧠 Sample Output

```text
🔎 Analyzing lines 1–80...

‼️ Vulnerability detected at line 33:
Code: typedef struct Book { ... }
Issue: No bounds checking on strings (`title`, `author`)
Suggested Fix: Use strncpy, and validate input length before copy

‼️ Vulnerability detected at line 101:
Code: int member_id;
Issue: Possible overflow with high user count
Suggested Fix: Add boundary check before assigning new member ID
```

---

## 🛠 Customization

You can edit `analyzer.py` to:

- Change the LLM model:
  ```python
  model = "gemma3:4b"
  ```
- Modify the prompt to suit your own rules
- Adjust chunk size for large files:
  ```python
  chunk_size = 80  # lines per chunk
  ```

---

## 🗂 Project Structure

```
.
├── analyzer.py        # Main CLI script
├── library.c          # Sample file for testing (optional)
├── README.md          # You’re reading it
├── venv/              # Python virtual environment (excluded from repo)
```
