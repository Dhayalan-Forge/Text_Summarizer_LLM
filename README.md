# Text Summarizer using LLM (T5-Small)

## Overview

This project is a **text summarization app** built using **Python**, **Hugging Face Transformers**, and **Streamlit**. It leverages the **T5-Small model** to generate concise summaries of input articles or text.

The app runs locally or can be deployed on **Streamlit Cloud** for easy web access.
Deployed App : **[Streamlit Cloud](https://textsummarizerllm.streamlit.app/)**

---

## Features

* Summarize articles, paragraphs, or any text input.
* Lightweight summarization using **T5-Small** (no large models required).
* Easy-to-use web interface with **Streamlit**.
* Can handle moderately long texts with chunking (optional enhancement).

---

## Installation

1. **Clone the repository**

```bash
git clone git@github.com:Dhayalan-Forge/Text_Summarizer_LLM.git
cd Text_Summarizer_LLM
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* Linux/macOS:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

### Run locally

```bash
python app.py
```

or using Streamlit:

```bash
streamlit run app.py
```

* Enter your text in the input box and click **Summarize**.
* The summary will appear below the input.

---

## Deployment

* This app can be deployed on **[Streamlit Cloud](https://share.streamlit.io/)**.
* Simply connect your GitHub repo and set `app.py` as the main file.
* No API keys are required if using the local **T5-Small model**.

---

## Folder Structure

```
Text_Summarizer_LLM/
│
├─ app.py            # Streamlit app
├─ summarizer.py     # Local testing script
├─ requirements.txt  # Python dependencies
├─ .gitignore        # Ignored files (.env, venv)
├─ README.md         # Project documentation
```
---

## License

This project is licensed under the **MIT License**.
