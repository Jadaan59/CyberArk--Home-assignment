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
- Docker & Docker Compose

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Jadaan59/CyberArk--Home-assignment.git
cd CyberArk--Home-assignment
```
## 🐳 Docker Setup
You can run Ollama in a container using the provided Dockerfile and docker-compose:

```bash
docker-compose up --build
```
This exposes Ollama on port 11434 and mounts the `data/` directory.

---

## 🏃 Usage
### Copy the required file to analyze into the data folder
```bash
cp <path_to_file> <repo_location>/data
```

### Open a new shell inside the container
```bash
docker exec -it <container-name> bash
```

### Analyze a C/C++ File
```bash
python3.12 analyzer.py <file_to_analze>
```
Replace `data/library.c` with your own C/C++ file as needed.

### Example Output
```
🔎 Analyzing lines 1–150...
‼️ Vulnerability detected at line 33:
Code: typedef struct Book { ... }
Issue: No bounds checking on strings (`title`, `author`)
Suggested Fix: Use strncpy, and validate input length before copy
```

---

## 🗂 Project Structure
```
CyberArk--Home-assignment/
├── data/
│   ├── analyzer.py        # Main CLI script
│   ├── library.c          # Sample C file for testing
│   └── deps/
│       └── requirements.txt # Python dependencies
├── docker-compose.yaml    # Docker Compose for Ollama
├── Dockerfile             # Dockerfile for container setup
├── README.md              # Project documentation
├── Report.md              # Work process and design notes
```