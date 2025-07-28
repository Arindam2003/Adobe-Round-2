# 📄 CHALLENGE_1A – PDF Heading Extractor

This project automatically extracts the **title and headings** (H1, H2, H3) from PDF documents using font size and style analysis with [PyMuPDF (`fitz`)](https://pymupdf.readthedocs.io/).

---

## 🚀 Features

- Detects headings in PDF files using font size and boldness
- Assigns heading levels dynamically (Title, H1, H2, H3)
- Outputs structured JSON with page numbers
- Dockerized for consistent runtime

---

## 🗂 Project Structure

```
CHALLENGE_1A/
├── app/
│   └── main.py                # Main script to extract headings
├── sample_dataset/
│   ├── pdfs/                  # Input PDFs
│   ├── output/                # Output JSON files
│   └── schema/                # (Optional) Any schema or metadata
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker image setup
├── README.md                  # Documentation
└── .venv/                     # Virtual environment (optional, local only)
```

---

## 📥 Input

- Drop PDF files inside `sample_dataset/pdfs/`.

## 📤 Output

- Extracted data will be saved as `.json` inside `sample_dataset/output/`.

---

## ⚙️ Local Run (Without Docker)

### 1. Install Dependencies

```bash
pip install -r requirements.txt

## 📦 Docker Image

•⁠  ⁠Image Name: amdipumondal/challenge_1a
•⁠  ⁠Available Tags: tagname
•⁠  ⁠Platform: python:3.10-slim

---

## 📥 Pull the Image

To pull the image from Docker Hub:

```bash
docker pull amdipumondal/challenge_1a:tagname