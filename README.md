
# 🩺 Insurance Document Chatbot (RAG + Gemini + ChromaDB)

An AI-powered Insurance Policy Question Answering System built using **Retrieval-Augmented Generation (RAG)**.

Users can upload one or more insurance policy PDFs, and the chatbot answers questions using the uploaded documents instead of relying on general knowledge.

---

## 🚀 Features

- 📄 Upload Single or Multiple Insurance PDFs
- 🤖 Gemini 3.5 Flash Integration
- 🧠 Sentence Transformer Embeddings (all-MiniLM-L6-v2)
- 📚 ChromaDB Vector Database
- 🔍 Semantic Search
- 💬 Interactive Chat Interface
- 📄 Source Chunk Display
- 📥 Download Chat History
- ⚡ Fast PDF Processing
- 🎨 Modern Streamlit UI
- 🔄 Typing Animation
- 📊 Chat Statistics

---

# 🏗️ Project Architecture

```
          PDF Upload
               │
               ▼
        PDF Text Extraction
               │
               ▼
         Text Cleaning
               │
               ▼
         Text Chunking
               │
               ▼
    SentenceTransformer
      (Embeddings)
               │
               ▼
          ChromaDB
               │
        Semantic Search
               │
               ▼
      Retrieved Context
               │
               ▼
      Gemini 3.5 Flash
               │
               ▼
        Final Answer
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Frontend |
| Gemini 3.5 Flash | Large Language Model |
| Sentence Transformers | Embeddings |
| ChromaDB | Vector Database |
| PDFPlumber | PDF Text Extraction |
| python-dotenv | API Key Management |

---

# 📂 Folder Structure

```
insurance-assistant/
│
├── app/
│   ├── config.py
│   ├── llm.py
│   ├── retriever.py
│   ├── vector_store.py
│   ├── process_pdf.py
│   ├── pdf_loader.py
│   ├── text_cleaner.py
│   ├── text_chunker.py
│   ├── summarizer.py
│
├── assets/
│   └── style.css
│
├── uploaded_files/
├── vector_db/
├── data/
│
├── streamlit_app.py
├── chat.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/insurance-document-chatbot.git

cd insurance-document-chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create Environment File

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## 5. Run the Application

```bash
streamlit run streamlit_app.py
```

---

# 💻 Usage

1. Upload one or more insurance policy PDFs.
2. Click **Process PDF(s)**.
3. Wait until the vector database is created.
4. Ask questions such as:

- What is the waiting period?
- What is covered?
- What is excluded?
- What is the claim process?
- What is the grace period?

The chatbot retrieves relevant document chunks and generates answers using Gemini 3.5 Flash.

---

# 📸 Screenshots

## Home Page

> Add screenshot here

```
screenshots/home.png
```

---

## PDF Upload

> Add screenshot here

```
screenshots/upload.png
```

---

## Chat Interface

> Add screenshot here

```
screenshots/chat.png
```

---

## Retrieved Source Chunks

> Add screenshot here

```
screenshots/source_chunks.png
```

---

# 📈 Future Enhancements

- ✅ Policy Comparison
- ✅ Voice Input
- ✅ Text-to-Speech
- ✅ OCR Support for Scanned PDFs
- ✅ Highlight Answer Source in PDF
- ✅ Conversation Memory
- ✅ User Authentication
- ✅ Cloud Database Integration
- ✅ Docker Deployment
- ✅ Multi-language Support

---

# 👨‍💻 Author

**Shiva Sai Ganesh Guda**

AI/ML Engineer | Python Developer | Generative AI Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ If you found this project useful, please give it a star!

