
import streamlit as st

st.set_page_config(
    page_title="EduPolicy AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 EduPolicy AI")
st.subheader("Intelligent Document Question Answering System")

st.write(
    "Upload your PDF or DOCX documents and ask questions "
    "based only on the uploaded documents."
)

st.divider()

uploaded_files = st.file_uploader(
    "Upload PDF or DOCX documents",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} document(s) uploaded successfully!")

    st.write("### Uploaded Documents")

    for file in uploaded_files:
        st.write(f"📄 {file.name}")

st.divider()

question = st.text_input(
    "Ask a question about your documents:"
)

if question:
    st.info("AI answer will appear here.")
