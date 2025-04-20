import streamlit as st
import cohere
import os
from dotenv import load_dotenv
from gtts import gTTS
import tempfile

# Load API key
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

# UI Title
st.set_page_config(layout="wide")
st.title("🦄 Dynamic Bedtime Story Creator & Narrator")

# User Inputs on Left
left_col, right_col = st.columns([1, 1])

with left_col:
    custom_prompt = st.text_area(
        "Custom Story Prompt (optional):", 
        placeholder="e.g. A unicorn who learns to sing under the stars"
    )
    length = st.slider("Story length (words):", 50, 300, 150)
    speed = st.radio("Reading Speed:", ["Normal", "Slow"])

# Session State
if "story" not in st.session_state:
    st.session_state.story = ""
if "audio_path" not in st.session_state:
    st.session_state.audio_path = ""

# Generate story
with left_col:
    if st.button("✨ Generate Story"):
        with st.spinner("Crafting your magical tale..."):
            prompt = custom_prompt.strip() if custom_prompt else "Write a magical bedtime story about a unicorn for kids."
            story = co.generate(
                model="command-r-plus",
                prompt=f"{prompt}\nMake it calming, imaginative, and {length} words long.",
                max_tokens=length * 2,
                temperature=0.9
            ).generations[0].text.strip()
            
            st.session_state.story = story
            st.session_state.audio_path = ""  # Reset audio
            st.success("Story ready!")

# Always show story on the right
with right_col:
    if st.session_state.story:
        st.subheader("📖 Your Story")
        st.markdown(f"<div style='font-size:18px; line-height:1.6'>{st.session_state.story}</div>", unsafe_allow_html=True)

# Generate & Play Audio
with left_col:
    if st.session_state.story and st.button("🔊 Read Aloud"):
        st.info("Generating audio...")
        tts = gTTS(text=st.session_state.story, lang='en', slow=(speed == "Slow"))

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.session_state.audio_path = fp.name

        st.success("Audio ready!")

# Show audio + download
with right_col:
    if st.session_state.audio_path:
        st.audio(st.session_state.audio_path, format="audio/mp3")
        with open(st.session_state.audio_path, "rb") as f:
            st.download_button(
                label="📥 Download MP3",
                data=f.read(),
                file_name="bedtime_story.mp3",
                mime="audio/mp3"
            )
