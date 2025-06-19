from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() # to load the .env file

# environment variables call
os.environ['OPENAI_API_KEY'] = "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"

# Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = "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"
os.environ['LANGCHAIN_TRACING_V2']="true"


# Creating Chatbot
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a help full assistant,Please provide response to the user queries"),
    ("user","Question:{question}")
    ]
)

# streamlit framework
st.title("ChatBot By Manunjay 😎")
input_txt=st.text_input("Search the topic you are looking for")

# open ai llm call
llm = ChatOpenAI(
    model="llama3-70b-8192",
    openai_api_key="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",
    openai_api_base="https://api.groq.com/openai/v1",
    temperature=0.7
)
output_parser = StrOutputParser()

# chain
chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'question':input_txt}))