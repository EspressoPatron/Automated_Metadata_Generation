import streamlit as st
import os
import json
from datetime import datetime
from langdetect import detect
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from docx import Document
from pdfminer.high_level import extract_text as extract_pdf_text
import pytesseract
import cv2

# ---- UTILITY FUNCTIONS ----

def extract_text_from_pdf(path):
    return extract_pdf_text(path)

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_text_from_image(path):
    image = cv2.imread(path)
    return pytesseract.image_to_string(image)

def extract_text_auto(path):
    ext = path.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(path)
    elif ext == 'docx':
        return extract_text_from_docx(path)
    elif ext == 'txt':
        return extract_text_from_txt(path)
    elif ext in ['jpg', 'jpeg', 'png']:
        return extract_text_from_image(path)
    else:
        return ""

def extract_keywords(text, top_n=10):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()

# Load summarizer once
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

# ---- STREAMLIT UI ----

st.title("📄 Automated Metadata Generator")

uploaded = st.file_uploader("Upload a PDF, DOCX, TXT, JPG, or PNG file", type=['pdf', 'docx', 'txt', 'jpg', 'png', 'jpeg'])

if uploaded:
    with st.spinner("🔍 Extracting content..."):
        filename = uploaded.name
        filepath = os.path.join("temp", filename)

        os.makedirs("temp", exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(uploaded.read())

        text = extract_text_auto(filepath)

        if not text or len(text.strip()) < 50:
            st.error("⚠️ Could not extract enough text from the document.")
        else:
            lang = detect(text)
            summary = summarizer(text[:1000], max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            keywords = extract_keywords(text)

            metadata = {
                "filename": filename,
                "extracted_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "language": lang,
                "summary": summary,
                "keywords": keywords.tolist(),
                "num_characters": len(text),
                "num_words": len(text.split())
            }

            st.success("✅ Metadata Generated!")

            st.subheader("🧾 Metadata")
            st.json(metadata)

            st.download_button(
                label="📥 Download Metadata JSON",
                data=json.dumps(metadata, indent=4),
                file_name=f"{filename.rsplit('.',1)[0]}_metadata.json",
                mime="application/json"
            )