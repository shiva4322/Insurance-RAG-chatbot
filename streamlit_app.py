import os
import time
import streamlit as st

from app.process_pdf import process_pdf
from app.summarizer import PolicySummarizer
from app.retriever import Retriever
from app.llm import GeminiLLM

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Insurance Assistant",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------------------------------
# Load CSS
# -----------------------------------------------------

def load_css():
    if os.path.exists("assets/style.css"):
        with open("assets/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# -----------------------------------------------------
# Initialize Session State
# -----------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

with st.sidebar:

    st.title("🩺 Insurance Assistant")

    st.success("🟢 System Ready")

    st.info("Upload → Process → Ask Questions")

    st.markdown("---")

    st.subheader("Technology Stack")

    st.write("🤖 **LLM:** Gemini 3.5 Flash")
    st.write("🧠 **Embeddings:** all-MiniLM-L6-v2")
    st.write("📚 **Vector DB:** ChromaDB")
    st.write("💻 **Framework:** Streamlit")

    st.markdown("---")

    st.subheader("Project")

    st.write("Insurance Policy Question Answering using RAG")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    uploaded_files = st.file_uploader(
        "📄 Upload Insurance PDFs",
        type=["pdf"],
        accept_multiple_files = True
    )

if uploaded_files:

    os.makedirs("uploaded_files", exist_ok=True)

    if st.button("📚 Process PDFs"):

        total_chunks = 0

        progress = st.progress(0)

        for index, uploaded_file in enumerate(uploaded_files):

            pdf_path = os.path.join(
                "uploaded_files",
                uploaded_file.name
            )

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            chunks = process_pdf(pdf_path)

            total_chunks += chunks

            status = st.empty()

            status.write(
                f"Processing {uploaded_file.name}"
            )

            progress.progress(
                (index + 1) / len(uploaded_files)

            )
        st.sidebar.metric(
            "Processed PDFs",
            len(uploaded_files) if uploaded_files else 0
        )
        st.success(
            f"""
Processed {len(uploaded_files)} PDFs

Total Chunks : {total_chunks}
"""
        )

        # ================= Policy Summary =================

        chunks = Retriever.retrieve(
            "Summarize this insurance policy",
            top_k=5
        )

        context = "\n\n".join(chunks)

        summary = PolicySummarizer.summarize(context)

        st.subheader("📄 Policy Summary")

        st.write(summary)

st.markdown("---")

chat_history = ""

for msg in st.session_state.messages:

    chat_history += f"{msg['role'].upper()}\n"

    chat_history += msg["content"]

    chat_history += "\n\n"

st.download_button(
    label="📥 Download Chat",
    data=chat_history,
    file_name="chat_history.txt",
    mime="text/plain"
)

# -----------------------------------------------------
# Main Page
# -----------------------------------------------------

st.title("🩺 Insurance Document Chatbot")

st.caption(
    "Powered by Gemini 3.5 Flash • ChromaDB • Sentence Transformers"
)

st.write(
    "Upload an insurance policy PDF and ask questions about it."
)

# -----------------------------------------------------
# Welcome Screen
# -----------------------------------------------------

if len(st.session_state.messages) == 0:

    st.info("""
👋 **Welcome!**

This chatbot can answer questions from your insurance policy.

### Steps

1. Upload an Insurance PDF
2. Click **Process PDF**
3. Ask your questions

### Example Questions

• What is the waiting period?

• What is covered?

• What is excluded?

• What is the grace period?

• What are the exclusions?
""")

# -----------------------------------------------------
# Display Previous Messages
# -----------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -----------------------------------------------------
# Chat Input
# -----------------------------------------------------

question = st.chat_input(
    "Ask your insurance question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.spinner("🤖 Searching Vector Database and Generating Answer..."):

        chunks = Retriever.retrieve(
            question,
            top_k=3
        )

        context = ""

        for i, chunk in enumerate(chunks, start=1):

            context += f"""

Document Chunk {i}

{chunk}

"""

        try:

            answer = GeminiLLM.generate_answer(
                context=context,
                question=question
            )

        except Exception as e:

            st.error(e)

            st.stop()

    with st.chat_message("assistant"):

        placeholder = st.empty()

        complete_answer = ""

        for word in answer.split():

            complete_answer += word + " "

            placeholder.markdown(complete_answer)

            time.sleep(0.02)

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Sources Retrieved",
                len(chunks)
            )

        with col2:

            st.metric(
                "Context Length",
                len(context)
            )

        with col3:

            st.metric(
                "Question Length",
                len(question)
            )

        st.markdown("---")

        with st.expander("📄 Source Chunks Used"):

            for i, chunk in enumerate(chunks, start=1):

                st.markdown(f"### Chunk {i}")

                st.write(chunk)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# -----------------------------------------------------
# Footer
# -----------------------------------------------------

st.markdown("---")

st.caption(
    "❤️ Built with Streamlit • Gemini 3.5 Flash • ChromaDB • Sentence Transformers"
)