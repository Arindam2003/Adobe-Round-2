# 📘 Challenge 1B - PDF Analyzer with Persona-Task Context

This project extracts, ranks, and summarizes the most relevant sections from PDF documents using a **persona** and a **task** as context. It's designed for automated information retrieval and summarization, and can be run standalone or inside a Docker container.

---

## 🚀 Features

- ✅ Extracts text sections from PDFs
- ✅ Ranks sections based on keyword overlap with persona & task
- ✅ Summarizes top-ranked sections
- ✅ Outputs structured JSON results per collection
- ✅ Dockerized for portable deployment

---

## 🗂️ Project Structure

```
challenge_1b/
├── main.py # Main analysis script
├── Dockerfile # Docker setup
├── requirements.txt # Python dependencies
├── README.md # You're reading it
├── .gitignore
├── .dockerignore
└── sample_structure/
├── Collection 1/
│ ├── challenge1b_input.json
│ └── PDFs/
│ └── doc1.pdf
```

# 🐳 Docker: Challenge 1B - PDF Analyzer

This Docker image (`amdipumondal/challenge_1b`) provides an out-of-the-box environment to extract, rank, and summarize relevant PDF sections based on persona and task inputs.

---

## 📦 Docker Image

- **Image Name:** `amdipumondal/challenge_1b`
- **Available Tags:** `tagname`
- **Platform:** `python:3.10-slim`

---

## 📥 Pull the Image

To pull the image from Docker Hub:

```bash
docker pull amdipumondal/challenge_1b:tagname