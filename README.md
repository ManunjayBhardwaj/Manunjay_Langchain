
# 🔗 LangChain Notebook: Exploring LLM Behavior with Ollama

This Jupyter Notebook explores how to use **LangChain** with local LLMs (such as **LLaMA 3.2** via **Ollama**) and demonstrates how the `temperature` parameter affects the creativity of model responses.

## 📘 Notebook Highlights

- 🔥 **Understanding `temperature`**: Learn how this parameter changes the randomness and creativity of LLM outputs.
- 💬 **LLM Invocation Example**: See how to call a language model using LangChain and Ollama.
- 🔄 **LLM Chains**: Utilize prompt templates and chains for more structured interactions.
- 🧠 **Memory in LangChain**: Understand how conversational memory is used to maintain context.
- 🤖 **Using Agents**: Learn how to build dynamic workflows using LangChain agents.

## 📂 Repository Contents

Alongside this notebook, the repository contains **other LangChain-based projects** that demonstrate advanced features, integrations, and use cases. Be sure to explore them as well!

## ⚙️ Requirements

Make sure you have the following installed:

```bash
pip install langchain langchain-community ollama
```

Ensure **Ollama** is set up and the `llama3.2` model is pulled:

```bash
ollama run llama3.2
```

## 🚀 Example Usage

```python
from langchain.chains.llm import LLMChain
from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2", temperature=0.7)
print(llm.invoke("Give solfege notes of Perfect by Ed Sheeran"))
```

## 📎 Tips

- `temperature = 0.0` → Deterministic responses
- `temperature = 0.7` → Balanced creativity
- `temperature > 1.0` → Highly random and imaginative

## 🧠 Explore More

Check out other **LangChain projects** in this repository to see additional applications, including agents, tools, and more advanced chains.

---

📁 Manunjay Bhardwaj
