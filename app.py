import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")
    
    st.header("Chat with multiple PDFs 📚")

    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        uploaded_files = st.file_uploader(
            "Upload your PDFs here and click on 'Process'",
            type="pdf",
            accept_multiple_files=True
        )
        if st.button("Process"):
            if uploaded_files:
                st.success(f"{len(uploaded_files)} PDFs uploaded successfully!")
            else:
                st.warning("Please upload at least one PDF.")
if __name__ == '__main__':
    main()
