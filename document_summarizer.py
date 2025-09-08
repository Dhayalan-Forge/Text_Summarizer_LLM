import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
import docx

# Load summarizer (deployment uses t5-base, local can use t5-small)
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

st.title("📄 Document Summarizer with Chunking")

uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + " "
    return text

def chunk_text(text, max_words=500):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i+max_words])

if uploaded_file:
    text = extract_text(uploaded_file)

    if text:
        st.subheader("📑 Extracted Text (Preview)")
        st.write(text[:1000] + "...")

        if st.button("Summarize"):
            chunks = list(chunk_text(text, max_words=500))
            summaries = []

            for i, chunk in enumerate(chunks):
                if len(chunk.split()) < 20:
                    continue  # skip very short chunks
                summary = summarizer(
                    chunk,
                    max_new_tokens=150,
                    min_length=30,
                    do_sample=False
                )
                summaries.append(summary[0]['summary_text'])

            # Combine summaries into one
            final_summary = " ".join(summaries)

            st.subheader("📝 Summary")
            st.write(final_summary)