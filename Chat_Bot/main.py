import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Set up secrets securely
os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]
os.environ['LANGCHAIN_API_KEY'] = st.secrets["LANGCHAIN_API_KEY"]
os.environ['LANGCHAIN_TRACING_V2'] = "true"

# Streamlit app UI
st.set_page_config(page_title="🧠 Chatbot by Manunjay")
st.title("🤖 ChatBot By Manunjay 😎")
input_txt = st.text_input("Ask a question or search a topic:")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's question clearly and concisely."),
    ("user", "Question: {question}")
])

# Groq (LLaMA3) model setup
llm = ChatOpenAI(
    model="gpt-4.1",
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    openai_api_base="https://api.openai.com/v1",
    temperature=0.7
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run chain on input
if input_txt:
    with st.spinner("Thinking..."):
        response = chain.invoke({'question': input_txt})
        st.success("✅ Answer:")
        st.markdown(response)
