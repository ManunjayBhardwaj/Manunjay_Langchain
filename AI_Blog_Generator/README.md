# 🧠 AI Blog Generator

Create high-quality blog posts in seconds using the power of **LLaMA3**, **LangChain**, and **Groq API** — all wrapped in a beautiful **Streamlit** interface.

---

## 🚀 Features

- 🧩 Generates detailed blog outlines
- 📄 Writes full-length blog articles
- 🧠 Provides 3-line summaries of the content
- 🎨 Clean, responsive UI with light/dark mode support
- ⚡ Powered by Groq-hosted **LLaMA3** via **LangChain**

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) — Web interface
- [LangChain](https://www.langchain.com/) — Prompt chaining
- [Groq API (OpenAI compatible)](https://groq.com/) — LLaMA3 LLM backend

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-blog-generator.git
cd ai-blog-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### Sample `requirements.txt`

```text
streamlit
langchain
openai
```

### 3. Set your API Key

Open `app.py` and replace the `openai_api_key` field:

```python
openai_api_key = "your-groq-api-key"
```

> Alternatively, you can load it from an environment variable:

```bash
export GROQ_API_KEY=your-key
```

And in `app.py`:

```python
import os
openai_api_key = os.getenv("GROQ_API_KEY")
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💡 How It Works

1. **User inputs a blog topic**
2. App uses LLaMA3 (via Groq) to:
   - Generate a blog outline
   - Write a full blog post from the outline
   - Summarize the blog into 3 lines
3. Results are displayed beautifully in Streamlit

---

## 🖼 Screenshots

| Input | Output |
|-------|--------|
| ![Input](screenshots/input.png) | ![Output](screenshots/output.png) |

---

## 👨‍💻 Author

Made with ❤️ by [Manunjay Bhardwaj](https://github.com/ManunjayBhardwaj)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🌐 Links

- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
