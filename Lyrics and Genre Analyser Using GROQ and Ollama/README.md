# 🎧 Song Analysis with LangChain, Ollama & Groq

This project uses **LangChain**, **Genius API**, and **LLMs (Ollama/Groq)** to:
- Fetch song lyrics from Genius.com
- Summarize the lyrics
- Predict the **genre** of the song

---

## 🧰 Features Covered

- ✅ LangChain's `LLMChain` and `SequentialChain`
- ✅ Local LLMs with [Ollama](https://ollama.com)
- ✅ Cloud-hosted models via [Groq API](https://console.groq.com/)
- ✅ Real-time lyrics fetch using `lyricsgenius` API
- ✅ Streamlit-ready code

---

## 📂 Files

- `app.py` or notebook: Core logic
- `README.md`: This file
- `requirements.txt`: Python dependencies

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/song-genre-predictor.git
cd song-genre-predictor
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, manually install:

```bash
pip install langchain langchain-community openai streamlit lyricsgenius
```

---

## 🔐 Genius API Setup

Create an account on [Genius](https://genius.com/developers) and get an access token.

Replace in code:

```python
genius = lyricsgenius.Genius("YOUR_API_KEY_HERE")
```

---

## 🧠 Ollama Model (Local)

To use `llama3.2` model:

1. Install Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Pull a model:
   ```bash
   ollama pull llama3
   ```

3. Run Ollama in background:
   ```bash
   ollama serve
   ```

---

## 🌐 Groq API Setup (Cloud)

Register on [Groq Console](https://console.groq.com/) and get your key.

Set this in code:

```python
llm = ChatOpenAI(
    model="llama3-70b-8192",
    openai_api_key="your_groq_key",
    openai_api_base="https://api.groq.com/openai/v1"
)
```

---

## 📊 Streamlit App (Optional UI)

To run as a web app:

```bash
streamlit run main.py
```

---

## 📝 Code Structure

### 1. **Basic Prompting**
- Uses Ollama or Groq to get direct LLM output.

### 2. **Single Chain Example**
- Simple prompt like: "What is the capital of {place}?"

### 3. **SequentialChain Example**
- Summarize a topic → Tweet it

### 4. **Lyrics-Based Chains**
- Fetch lyrics → Summarize → Detect genre

### 5. **Groq Integration**
- Same as above but with Groq-hosted models

---

## 📦 Sample Output

```
🎤 Original Lyrics:
[Tons of lyrical content...]

💡 Lyrics Summary:
A song about spiritual longing and divine love.

🎵 Genre:
Sufi
```

---

## 🤝 Credits

- LangChain
- Ollama
- Groq
- Genius Lyrics API

---

## 🛡️ License

MIT License — feel free to fork and use!
