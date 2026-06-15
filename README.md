# 🏛️ Delhi Tourism Assistant (RAG Pipeline)

A highly responsive, production-ready Retrieval-Augmented Generation (RAG) application that acts as an expert tour guide for Delhi. The system pairs local domain knowledge extracted from document datasets with the advanced reasoning capabilities of Google's modern `gemini-2.5-flash` model via the native `google-genai` SDK.

---

## 🚀 Key Features

* **Semantic Text Retrieval:** Chunks and indexes custom local datasets (like PDFs) into a dense vector space using Hugging Face embeddings.
* **Vector Search Acceleration:** Implements a localized `FAISS` index structure for sub-millisecond similarity context matching.
* **Modern AI Integration:** Fully migrated to the modern native `google-genai` SDK framework.
* **Intelligent Fallback Architecture:** System prompt constraints balance strict document ground-truth data with generalized backing knowledge for holistic user queries.
* **Streamlit Interactive Dashboard:** Clean, user-friendly interactive interface built entirely using Python.

---

## 🛠️ Tech Stack & Architecture

* **Frontend UI:** Streamlit
* **LLM Orchestration:** Google GenAI SDK (`gemini-2.5-flash`)
* **Vector Store:** FAISS (Facebook AI Similarity Search)
* **Document Processing:** PyMuPDF (`fitz`) / Pickle
* **Environment Management:** Python Dotenv (`python-dotenv`)

---

## 📂 Project Structure

```text
DelhiTourismRAG/
├── data/
│   └── delhi_facts.pdf       # Local knowledge base dataset
├── src/
│   ├── __init__.py
│   ├── chunker.py            # Logic for parsing and slicing text chunks
│   ├── embedder.py           # Generates semantic dense vector representations
│   ├── llm.py                # Native Google GenAI integration functions
│   ├── pdf_loader.py         # Document parsing using PyMuPDF
│   ├── rag.py                # Core orchestration layer (Retrieval + Stuffing)
│   └── retriever.py          # Similarity search and FAISS index matching
├── vectorstore/
│   ├── chunks.pkl            # Serialized string data for context injection
│   └── faiss.index           # Compiled vector matrix database
├── .env                      # Local environment configurations (ignored by git)
├── .gitignore                # Specifies intentionally untracked files to exclude
├── app.py                    # Main Streamlit user interface dashboard entrypoint
└── requirements.txt          # Defined python package dependencies
