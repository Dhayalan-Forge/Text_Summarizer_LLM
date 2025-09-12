# 📝 Unified Text & Document Summarizer

A summarization app built with **Python**, **Hugging Face Transformers**, and **Streamlit**. It allows you to either **enter text manually** or **upload a PDF/DOCX file** and get a concise summary. The app uses **T5 models** (`t5-small` for local testing, `t5-base` for deployment) to generate summaries.

---

## 🚀 Features

* ✍️ **Text Summarization**: Paste or type any text to get a summary.
* 📄 **Document Summarization**: Upload PDFs or Word docs for summarization.
* ⚡ **Chunking Support**: Handles long documents by splitting them into smaller parts.
* 🔄 **Dynamic Length**: Adjusts summary size based on input length.
* 🌐 **Deployable on Streamlit Cloud**.

---

## 📂 Project Structure

````

Text\_Summarizer\_LLM/
├── summarizer\_app.py     \# Unified app (text + document summarizer)
├── requirements.txt      \# Project dependencies
├── README.md             \# Documentation
├── LICENSE               \# MIT License
├── .gitignore
└── .devcontainer/        \# (Optional) Dev container configuration

````

---

## ⚙️ Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd Text_Summarizer_LLM
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate the environment:**
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```
    * **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Run the App

Start the unified summarizer with this command:

```bash
streamlit run summarizer_app.py
````

  * Choose **"✍️ Enter Text"** to summarize text directly.
  * Choose **"📄 Upload Document"** to upload a PDF or DOCX file.

-----

## 📌 Requirements (`requirements.txt`)

```ini
streamlit==1.49.1
transformers==4.56.1
torch==2.8.0
PyPDF2==3.0.1
python-docx==1.1.2
```

-----

## 🌐 Deployment

To deploy this app:

1.  Push the repository to GitHub.
2.  Deploy directly on Streamlit Cloud.
3.  The deployed version automatically uses **`t5-base`** for higher accuracy.

-----

## 🔗 Live Demo

👉 [Streamlit App](https://textsummarizerllm-mkrccy2azj9g2tvzbuekrb.streamlit.app/)

-----

## 📜 License

This project is licensed under the MIT License see the `LICENSE` file for details.
