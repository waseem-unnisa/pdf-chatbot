# AI PDF Chatbot 🤖

A Retrieval-Augmented Generation (RAG) web application built with Streamlit, LangChain, and Google Gemini. This application allows users to upload a PDF document, process its content into a vector database, and ask contextual questions about the document's contents.

## 🚀 Features
* **PDF Ingestion:** Upload any standard PDF file through a clean user interface.
* **Smart Chunking:** Automatically splits document text into manageable pieces for accurate retrieval.
* **Vector Storage:** Embeds text chunks and stores them efficiently using Chroma DB.
* **Contextual Q&A:** Answers user questions using Google's Generative AI models based strictly on the uploaded document's context.

## 🛠️ Tech Stack
* **Frontend UI:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/)
* **Embedding & LLM Provider:** Google Generative AI (Gemini)
* **Vector Database:** Chroma DB

## 📋 Prerequisites
Before running the project, ensure you have Python installed (Python 3.9 to 3.11 is recommended for library stability) and a Google Gemini API Key.

