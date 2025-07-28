import os
import json
import fitz  # PyMuPDF
from nltk.tokenize import sent_tokenize
from tqdm import tqdm

# ====== Configuration ======
COLLECTIONS = ["Collection 1", "Collection 2", "Collection 3"]

# ====== Input/Output Utilities ======

def load_input_config(folder):
    input_path = os.path.join(folder, "challenge1b_input.json")
    with open(input_path, "r") as f:
        return json.load(f)

def write_output_config(folder, output_data):
    output_path = os.path.join(folder, "challenge1b_output.json")
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)
    print(f"✅ Output saved to {output_path}")

# ====== PDF Section Extraction ======

def extract_sections_from_pdf(filepath):
    doc = fitz.open(filepath)
    sections = []
    for page_number in range(len(doc)):
        text = doc[page_number].get_text()
        if text.strip():
            first_line = text.split('\n')[0]
            sections.append({
                "page_number": page_number + 1,
                "section_title": first_line[:60],
                "text": text
            })
    return sections

# ====== Ranking Sections by Persona & Task ======

def rank_sections(sections, persona, task):
    keywords = (persona + " " + task).lower().split()
    for section in sections:
        score = sum(1 for word in keywords if word in section["text"].lower())
        section["importance_rank"] = score
    return sorted(sections, key=lambda s: -s["importance_rank"])

# ====== Lightweight Summary ======

def summarize_text(text, persona, task):
    try:
        sentences = sent_tokenize(text)
        return " ".join(sentences[:3]) if sentences else text[:300]
    except:
        return text[:300]

# ====== Main Logic Per Collection ======

def process_collection(collection_folder):
    try:
        input_data = load_input_config(collection_folder)
    except FileNotFoundError:
        print(f"❌ Missing input JSON in {collection_folder}")
        return

    persona = input_data["persona"]["role"]
    task = input_data["job_to_be_done"]["task"]
    documents = input_data["documents"]

    extracted_sections = []
    subsection_analysis = []

    for doc in tqdm(documents, desc=f"📄 Processing {collection_folder}"):
        pdf_path = os.path.join(collection_folder, "PDFs", doc["filename"])

        if not os.path.exists(pdf_path):
            print(f"⚠️ File not found: {pdf_path}")
            continue

        sections = extract_sections_from_pdf(pdf_path)
        ranked = rank_sections(sections, persona, task)

        for rank, section in enumerate(ranked[:3], start=1):  # Top 3 ranked
            extracted_sections.append({
                "document": doc["filename"],
                "section_title": section["section_title"],
                "importance_rank": rank,
                "page_number": section["page_number"]
            })

            summary = summarize_text(section["text"], persona, task)
            subsection_analysis.append({
                "document": doc["filename"],
                "refined_text": summary,
                "page_number": section["page_number"]
            })

    if extracted_sections:
        output = {
            "metadata": {
                "input_documents": [d["filename"] for d in documents],
                "persona": persona,
                "job_to_be_done": task
            },
            "extracted_sections": extracted_sections,
            "subsection_analysis": subsection_analysis
        }
        write_output_config(collection_folder, output)
    else:
        print(f"⚠️ No valid sections found in: {collection_folder}")

# ====== Entry Point ======

def main():
    import nltk
    nltk.download('punkt')  # Ensures sentence tokenizer is available

    print("📘 Starting Analysis for All Collections...\n")
    for folder in COLLECTIONS:
        if os.path.exists(folder):
            process_collection(folder)
        else:
            print(f"⚠️ Skipping missing folder: {folder}")
    print("\n✅ All done! Output saved per collection.")

if __name__ == "__main__":
    main()
