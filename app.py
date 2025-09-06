import streamlit as st
from transformers import pipeline

st.title("📄 Text Summarizer (T5 Small)")

# Load model once
summarizer = pipeline("summarization", model="t5-small")

# Input text
user_input = st.text_area("Enter your text here", height=250)

# Summarize button
if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Generating summary... ⏳"):
            summary = summarizer(user_input, max_length=100, min_length=30, do_sample=False)
            st.success(summary[0]['summary_text'])
