# 🤖 ChatBot by Manunjay 😎

A Streamlit-based chatbot that leverages **LangChain**, **Groq's LLaMA3-70B** model (OpenAI-compatible), and **LangSmith** for tracing. It provides helpful responses to user queries in a clean, interactive web app.

---
## 🚀 Working link

-https://manunjay-chat-bot.streamlit.app

---

## 🚀 Features

- ✅ Built with **Streamlit**
- ✅ Uses **LangChain** to manage LLM prompts
- ✅ Powered by **Groq’s LLaMA3-70B** via OpenAI-compatible API
- ✅ Secure API key handling with `.env`
- ✅ LangSmith tracing for monitoring and debugging

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a `.env` File

In the root directory, create a file named `.env` and add your keys:

```env
OPENAI_API_KEY=gsk_your_groq_key
LANGCHAIN_API_KEY=lsv2_your_langsmith_key
```

> ⚠️ Never commit this file to GitHub.

---

### 3. Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, use this:

```txt
streamlit
langchain
langchain-core
langchain-openai
python-dotenv
```

---

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

You’ll see the chatbot UI open in your browser. Enter a query and get instant AI-generated responses using LLaMA3!

---

## 🧠 Tech Stack

- **Streamlit** – Frontend framework
- **LangChain** – LLM framework for chaining prompts
- **Groq API** – LLaMA3-70B model with blazing fast inference
- **LangSmith** – Prompt tracing and analytics
- **python-dotenv** – For secure key management

---

## 📸 Sample UI

*(Add screenshot.png here if needed)*

---

## 🔐 Best Practices

- ✅ Keep `.env` in your `.gitignore`
- ❌ Don't hardcode API keys in code
- ✅ Use LangSmith for prompt debugging
- ✅ Keep `temperature` between `0.5 - 0.9` for more natural replies

---

## 🙋‍♂️ Developed by

**Manunjay Bhardwaj**  
🔗 [Portfolio](https://manunjaybhardwaj.netlify.app/)  
🐙 [GitHub](https://github.com/ManunjayBhardwaj)  
📧 manunjay09@gmail.com  

---

## 📜 License

MIT License – Free to use and modify.
