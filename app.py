import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon="📚")

    st.header("📚 Chat with multiple PDFs")

    with st.sidebar:
        st.subheader("Your documents")
        uploaded_files = st.file_uploader(
            "Upload your PDFs here",
            type="pdf",
            accept_multiple_files=True
        )

    # Show file upload results
    if uploaded_files:
        st.success(f"{len(uploaded_files)} PDFs uploaded successfully!")

        st.markdown("### File Names:")
        for file in uploaded_files:
            st.markdown(f"- {file.name}")

    else:
        st.info("Please upload at least one PDF.")

    # Chat section
    question = st.text_input("Ask a question about your documents:")
    if question:
        st.write(f"You asked: `{question}`")
        st.info("This is just a placeholder. We'll connect to LLM next.")

if __name__ == '__main__':
    main()
