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

# Text Extraction Functions

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

# Chunked Summarization & Keywords

def split_into_chunks(text, max_chars=1000):
    paragraphs = text.split('\n')
    chunks, current = [], ''
    for para in paragraphs:
        if len(current) + len(para) < max_chars:
            current += para + '\n'
        else:
            chunks.append(current.strip())
            current = para + '\n'
    if current:
        chunks.append(current.strip())
    return chunks

def summarize_text_limited(text, summarizer, max_chars=1000, max_chunks=3):
    chunks = split_into_chunks(text, max_chars)
    summaries = []
    for i, chunk in enumerate(chunks[:max_chunks]):
        try:
            result = summarizer(chunk, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            summaries.append(result)
        except Exception as e:
            print(f"Chunk {i} skipped: {e}")
    return "\n".join(summaries)

def extract_keywords(text, top_n=10):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()

# Streamlit App

st.set_page_config(page_title="Auto Metadata Generator", page_icon="📄")
st.title("Automated Metadata Generator")

uploaded = st.file_uploader("Upload PDF, DOCX, TXT, JPG, or PNG", type=["pdf", "docx", "txt", "jpg", "jpeg", "png"])

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

if uploaded:
    with st.spinner("🔍 Processing document..."):
        filename = uploaded.name
        temp_path = os.path.join("temp", filename)
        os.makedirs("temp", exist_ok=True)

        with open(temp_path, "wb") as f:
            f.write(uploaded.read())

        text = extract_text_auto(temp_path)

        if not text or len(text.strip()) < 50:
            st.error("Insufficient content extracted.")
        else:
            lang = detect(text)
            summary = summarize_text_limited(text, summarizer)
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

            st.success("Metadata Generated")
            st.subheader("Metadata")
            st.json(metadata)

            st.download_button(
                "Download Metadata JSON",
                data=json.dumps(metadata, indent=4),
                file_name=f"{filename.rsplit('.',1)[0]}_metadata.json",
                mime="application/json"
            )

# st.sidebar.image("https://images.app.goo.gl/9RxHnDF9HV9PM3Qx7", use_column_width=True)
# st.sidebar.markdown("#### Auto Metadata Generator")