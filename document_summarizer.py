import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
import docx

# Load summarizer (local T5-small model)
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

st.title("📄 Document Summarizer")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file:
    text = ""

    if uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            text += page.extract_text() + " "

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + " "

    if text:
        st.subheader("📑 Extracted Text")
        st.write(text[:1000] + "...")  # show preview

        # --- Dynamic summary length ---
        word_count = len(text.split())
        if word_count > 500:
            max_len = 250
            min_len = 100
        else:
            max_len = 100
            min_len = 30

        if st.button("Summarize"):
            summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            st.subheader("📝 Summary")
            st.write(summary[0]['summary_text'])