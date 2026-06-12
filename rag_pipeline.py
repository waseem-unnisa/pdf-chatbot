import os
from dotenv import load_dotenv
load_dotenv()

from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma 
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def load_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    all_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:  # only append if text is not None
            all_text.append(text)

    return "\n".join(all_text)

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    return [chunk for chunk in chunks if chunk.strip()]

def create_vector_store(chunks):
    api_key = os.getenv("GOOGLE_API_KEY")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )
    vector_store = Chroma(
        collection_name="pdf_collection",
        embedding_function=embeddings
    )
    
    if chunks:
        vector_store.add_texts(texts=chunks)
        
    return vector_store

def get_answer(vector_store, question):
    api_key = os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    
    prompt = ChatPromptTemplate.from_template("""
    Answer the question based on the context below.
    
    Context: {context}
    
    Question: {question}
    """)
    
    retriever = vector_store.as_retriever()
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain.invoke(question)

def main():

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("\n[ERROR] GOOGLE_API_KEY is completely missing!")
        return
    
    pdf_path = "OOAD.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"Error: Could not find the file '{pdf_path}' in your directory.")
        return

    print("Extracting text from PDF...")
    text = load_pdf(pdf_path)

    print("Splitting text into chunks...")
    text_chunks = split_text(text)
    
    print("Creating vector store...")
    vector_store = create_vector_store(text_chunks)
    
    query = "what is this document about?"
    print(f"Asking Gemini: '{query}'...")
    answer = get_answer(vector_store, query)

    print("\n---- Gemini's Answer")
    print(answer)

if __name__ == "__main__":
    main()






   
        
                  
    

       










 