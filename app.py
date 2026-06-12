import streamlit as st
from rag_pipeline import load_pdf, split_text, create_vector_store, get_answer

def main():
    st.set_page_config(
    page_title =  "PDF ChatBot",
    page_icon = "📄",
    layout = "centered"
)
with st.container():
    st.title("AI PDF Chatbot 🤖")

    if create_vector_store not in st.session_state:
        st.session_state["create_vector_store"] = None


uploaded_file = st.file_uploader(type="pdf", label= "Upload your PDF here!")
user_question = st.text_input("Ask a question about the pdf:")

    
if st.button("submit"):
        if uploaded_file is not None:
            with st.spinner ("Processing the pdf..."):
             

             pdf = load_pdf(uploaded_file)

             text_chunk = split_text(pdf)

             st.session_state["create_vector_store"] = create_vector_store(text_chunk)

if user_question:
             answer = get_answer(st.session_state["create_vector_store"], user_question)
             st.write(answer)

else:
       
       st.error("Please type a question in the text box before hitting submit!")
       

if __name__ == "__main__":
   main()



            






