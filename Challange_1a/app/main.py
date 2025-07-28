import fitz  # PyMuPDF
import os
import json
from pathlib import Path
from collections import Counter


def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    candidates = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                if not spans:
                    continue
                text = "".join([span["text"] for span in spans]).strip()
                if not text or len(text.split()) < 3:
                    continue
                font_size = round(spans[0]["size"], 1)  # normalize slight variations
                bold = bool(spans[0]["flags"] & 2)
                candidates.append({
                    "text": text,
                    "size": font_size,
                    "bold": bold,
                    "page": page_num
                })

    if not candidates:
        return {
            "title": "Untitled Document",
            "outline": []
        }

    # Get all unique font sizes sorted from largest to smallest
    all_sizes = sorted({c["size"] for c in candidates}, reverse=True)

    # Find the most common font size → assume body text
    body_size = Counter([c["size"] for c in candidates]).most_common(1)[0][0]

    title_size = all_sizes[0]
    h1_size = all_sizes[1] if len(all_sizes) > 1 else body_size
    h2_size = all_sizes[2] if len(all_sizes) > 2 else body_size

    outline = []
    title = ""

    for c in candidates:
        if c["size"] == title_size:
            title = c["text"]
        elif c["size"] == h1_size:
            outline.append({"level": "H1", "text": c["text"], "page": c["page"]})
        elif c["size"] == h2_size:
            outline.append({"level": "H2", "text": c["text"], "page": c["page"]})
        elif c["size"] > body_size:
            outline.append({"level": "H3", "text": c["text"], "page": c["page"]})

    return {
        "title": title or "Untitled Document",
        "outline": outline
    }

def main():
    # input_dir = Path("/app/input")
    # output_dir = Path("/app/output")

    input_dir = Path("sample_dataset/pdfs")
    output_dir = Path("sample_dataset/output")

    for pdf_file in input_dir.glob("*.pdf"):
        print(f"Processing: {pdf_file.name}")
        result = extract_headings(pdf_file)
        out_path = output_dir / f"{pdf_file.stem}.json"
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"✅ Output written: {out_path}")

if __name__ == "__main__":
    main()