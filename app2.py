import streamlit as st
import os
from PIL import Image

from mic import transcribe_audio
from tts import text_to_speech
from ocr import extract_text_from_image
from text_summarization import summarize_text_with_rag

st.set_page_config(
    page_title="Multimodal AI Assistant",
    layout="wide"
)

os.makedirs("outputs", exist_ok=True)

st.title("Multimodal AI Assistant")
st.caption("Speech, Vision, Text, and RAG-based Intelligence")

tab1, tab2, tab3, tab4 = st.tabs([
    "Speech to Text",
    "Image Summary",
    "Text to Speech",
    "RAG Summarizer"
])


# -------------------- TAB 1 --------------------

with tab1:
    st.header("Speech to Text")

    audio_file = st.file_uploader(
        "Upload a WAV file",
        type=["wav"]
    )

    if audio_file:
        file_path = f"outputs/{audio_file.name}"

        with open(file_path, "wb") as f:
            f.write(audio_file.getbuffer())

        if st.button("Transcribe Audio"):
            with st.spinner("Transcribing..."):
                text = transcribe_audio(file_path)

            st.success("Transcription completed")
            st.text_area("Transcribed Text", text, height=150)


# -------------------- TAB 2 --------------------

with tab2:
    st.header("Image Understanding and Summary")

    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, use_column_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing image..."):
                image_path = f"outputs/{uploaded_image.name}"
                image.save(image_path)
                summary = extract_text_from_image(image_path)

            st.success("Summary generated")
            st.text_area("Image Summary", summary, height=120)


# -------------------- TAB 3 --------------------

with tab3:
    st.header("Text to Speech")

    input_text = st.text_area(
        "Enter text",
        height=150
    )

    if st.button("Convert to Speech"):
        if input_text.strip():
            with st.spinner("Generating speech..."):
                audio_path = text_to_speech(input_text)

            st.success("Speech generated")
            st.audio(audio_path)
        else:
            st.warning("Please enter text")


# -------------------- TAB 4 --------------------

with tab4:
    st.header("Document Summarization using RAG")

    uploaded_file = st.file_uploader(
        "Upload a text file",
        type=["txt"]
    )

    if uploaded_file:
        file_path = f"outputs/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Generate Summary"):
            with st.spinner("Running RAG..."):
                summary = summarize_text_with_rag(file_path)

            st.success("Summary generated")
            st.markdown(summary)


st.markdown("---")
st.caption("Built using Whisper, Vision AI, LangChain, FastAPI and Streamlit")