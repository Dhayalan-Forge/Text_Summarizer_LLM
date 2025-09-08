# 📘 Text Summarizer using LLMs

This project demonstrates a **text summarization tool** built with Hugging Face Transformers and Streamlit.  
It supports both **direct text summarization** and **document upload (PDF/DOCX) summarization**.

---

## 🚀 Project Features
- **Text Summarizer (`app.py`)**  
  - Simple Streamlit app.  
  - Uses **`t5-small`** for lightweight, local testing.  

- **Document Summarizer (`document_summarizer.py`)**  
  - Upload **PDF/DOCX** files and get extracted summaries.  
  - Supports **dynamic summary length** (longer docs → longer summaries).  
  - Uses **`t5-base`** for more accurate results when deployed.  

---

## 📂 Project Structure
```
Text\_Summarizer\_LLM/
│── app.py                  # Basic text summarizer
│── document\_summarizer.py  # PDF/DOCX summarizer (deploy-ready)
│── summarizer.py           # (Optional) helper functions
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── LICENSE                 # MIT License
│── .gitignore
│
├── docs/
│   └── llm\_cheatsheet.pdf  # (optional guide)
└── examples/
└── sample\_text.txt
└── sample\_summary.txt
```
---
## Installation

1. Clone the repo:
```bash
git clone https://github.com/Dhayalan-Forge/Text_Summarizer_LLM.git
cd Text_Summarizer_LLM
```

2. Create virtual environment:

```bash
python -m venv venv
```

3. Activate environment:

* **Windows (PowerShell)**:

```powershell
.\venv\Scripts\activate
```

* **Linux/macOS**:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Apps

### 1. Run Basic Text Summarizer (local)

```bash
streamlit run app.py
```

* Uses **`t5-small`** (fast, lightweight).

### 2. Run Document Summarizer (local or deployed)

```bash
streamlit run document_summarizer.py
```

* Locally → still works with **`t5-small`** if you want.
* Deployment (Streamlit Cloud) → switches to **`t5-base`** automatically for better accuracy.

---

## 📌 Requirements.txt

Make sure this file contains:

```
transformers
torch
streamlit
PyPDF2
python-docx
```

---

## 🌍 Deployment

* Push this repo to GitHub.
* Deploy directly on **Streamlit Cloud**.
* For best results, `document_summarizer.py` will use **`t5-base`** (≈220MB).

---

## 📎 Live Demo

👉 [Streamlit Deployed App](https://textsummarizerllm.streamlit.app/)

---