import streamlit as st
from transformers import pipeline
from PyPDF2 import PdfReader
import docx

# Load summarizer (use t5-small locally, t5-base when deployed)
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")

st.title("📝 Unified Text & Document Summarizer")

# ---------- Helper Functions ----------
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

def summarize_text(input_text):
    chunks = list(chunk_text(input_text, max_words=500))
    summaries = []

    for chunk in chunks:
        if len(chunk.split()) < 20:
            continue
        summary = summarizer(
            chunk,
            max_new_tokens=150,
            min_length=30,
            do_sample=False
        )
        summaries.append(summary[0]['summary_text'])

    # Combine all chunk summaries
    return " ".join(summaries)

# ---------- Streamlit UI ----------
option = st.radio("Choose input type:", ["✍️ Enter Text", "📄 Upload Document"])

if option == "✍️ Enter Text":
    user_text = st.text_area("Enter your text here:", height=200)

    if st.button("Summarize Text"):
        if len(user_text.split()) < 20:
            st.warning("Please enter at least 20 words for summarization.")
        else:
            summary = summarize_text(user_text)
            st.subheader("📝 Summary")
            st.write(summary)

elif option == "📄 Upload Document":
    uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])

    if uploaded_file:
        extracted_text = extract_text(uploaded_file)
        st.subheader("📑 Extracted Text (Preview)")
        st.write(extracted_text[:1000] + "...")

        if st.button("Summarize Document"):
            if len(extracted_text.split()) < 20:
                st.warning("The document does not have enough text to summarize.")
            else:
                summary = summarize_text(extracted_text)
                st.subheader("📝 Summary")
                st.write(summary)
