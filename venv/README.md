# 📚 Wikipedia Chat Agent using LangChain & Hugging Face

This project is a simple yet powerful conversational agent that combines **LangChain**, **Wikipedia**, and **Hugging Face** models via API. It answers user queries by retrieving relevant summaries from Wikipedia and generating responses using a lightweight language model.

## 🚀 Features

- 🌐 Wikipedia search integration via LangChain `Tool`
- 🤖 Uses Hugging Face hosted model (`flan-t5-base`) — *no downloads required*
- 📏 Adjustable sentence count from Wikipedia
- 💬 Conversation history tracking
- ⚡ Clean, fast UI built with Streamlit

---

## 📦 Setup

> Python 3.10 or 3.11 is recommended. Python 3.13 may cause compatibility issues with some packages like NumPy and Torch.

### 1. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

