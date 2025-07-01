import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

# ----------------------- Setup LLM -----------------------
llm = ChatOpenAI(
    model="gpt-4.1",  # GPT-4.1 model ID on OpenAI
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    temperature=0.7
)

# ----------------------- Define Chains -----------------------
outline_prompt = PromptTemplate.from_template(
    "Create a detailed blog outline for the topic:\n\n{topic}"
)
outline_chain = LLMChain(llm=llm, prompt=outline_prompt, output_key="outline")

blog_prompt = PromptTemplate.from_template(
    "Write a detailed blog article based on the following outline:\n\n{outline}"
)
blog_chain = LLMChain(llm=llm, prompt=blog_prompt, output_key="blog")

summary_prompt = PromptTemplate.from_template(
    "Summarize the following blog article in exactly 3 concise lines:\n\n{blog}"
)
summary_chain = LLMChain(llm=llm, prompt=summary_prompt, output_key="summary")

blog_generator_chain = SequentialChain(
    chains=[outline_chain, blog_chain, summary_chain],
    input_variables=["topic"],
    output_variables=["outline", "blog", "summary"],
    verbose=True
)

# ----------------------- Streamlit UI -----------------------

st.set_page_config(page_title="🧠 AI Blog Generator", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 AI Blog Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Create amazing blog articles using <strong>GPT-4.1</strong> + <strong>LangChain</strong> 🚀</p>", unsafe_allow_html=True)

topic = st.text_input("🎯 Enter a blog topic", placeholder="e.g., The Future of Renewable Energy")

if st.button("Generate Blog") and topic:
    with st.spinner("Generating... Please wait ⏳"):
        try:
            result = blog_generator_chain.invoke({"topic": topic})

            st.markdown("## 🧩 Generated Outline")
            st.markdown(f"""<div style='padding:1em; background-color:#E8F5E9; border-radius:10px; color:#000;'>{result['outline']}</div>""", unsafe_allow_html=True)

            st.markdown("## 📄 Blog Article")
            st.markdown(f"""<div style='padding:1em; background-color:#FFF3E0; border-radius:10px; color:#000;'>{result['blog']}</div>""", unsafe_allow_html=True)

            st.markdown("## 🧠 3-Line Summary")
            st.markdown(f"""<div style='padding:1em; background-color:#E3F2FD; border-radius:10px; font-weight:bold; color:#000;'>{result['summary']}</div>""", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    st.markdown("👆 Enter a topic and click **Generate Blog** to get started!")

# ----------------------- Footer -----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; font-size: 0.9em; color: gray;'>
    Made with ❤️ using <a href="https://www.langchain.com" target="_blank">LangChain</a> +
    <a href="https://openai.com" target="_blank">OpenAI</a> by
    <a href="https://github.com/ManunjayBhardwaj" target="_blank">Manunjay Bhardwaj</a>
</div>
""", unsafe_allow_html=True)
