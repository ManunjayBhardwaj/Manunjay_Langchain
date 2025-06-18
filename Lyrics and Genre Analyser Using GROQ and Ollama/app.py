import streamlit as st
import lyricsgenius
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# --- SETUP ---

GENIUS_API_KEY = "6zjxdsJMvjbAOVYWfIJ0o2cb5y_Dx0mWXwg_7aJDfKpBcr4VrNBAfN_TPZE4Ob2y"
GROQ_API_KEY = "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"

# Genius client
genius = lyricsgenius.Genius(GENIUS_API_KEY, remove_section_headers=True)

# Groq LLM
llm = ChatOpenAI(
    model="llama3-70b-8192",
    openai_api_key=GROQ_API_KEY,
    openai_api_base="https://api.groq.com/openai/v1",
    temperature=0.7
)

# Chains
lyrics_prompt = PromptTemplate.from_template("Summarize the following lyrics:\n\n{lyrics}")
lyrics_chain = LLMChain(llm=llm, prompt=lyrics_prompt, output_key="summary")

genre_prompt = PromptTemplate.from_template(
    "Identify the genre of the song based on this summary. Give a single word output:\n\n{summary}"
)
genre_chain = LLMChain(llm=llm, prompt=genre_prompt, output_key="genre")

overall_chain = SequentialChain(
    chains=[lyrics_chain, genre_chain],
    input_variables=["lyrics"],
    output_variables=["summary", "genre"],
    verbose=False
)

# --- STREAMLIT UI ---

st.title("🎵 Lyrics Genre Classifier with Groq + Genius")
st.markdown("Get song lyrics, summarize them, and identify the genre using LLaMA3 (Groq).")

song_name = st.text_input("Enter Song Name", value="Bulleya")
artist_name = st.text_input("Enter Artist Name", value="Arijit Singh")

if st.button("Analyze"):
    with st.spinner("Fetching lyrics and analyzing..."):
        try:
            song_obj = genius.search_song(song_name, artist_name)
            lyrics = song_obj.lyrics if song_obj and song_obj.lyrics else "Lyrics not found."

            result = overall_chain.invoke({"lyrics": lyrics})

            st.subheader("🎤 Original Lyrics")
            st.text_area("", lyrics, height=300)

            st.subheader("💡 Summary")
            st.write(result["summary"])

            st.subheader("🎵 Predicted Genre")
            st.success(result["genre"])

        except Exception as e:
            st.error(f"Something went wrong: {e}")
