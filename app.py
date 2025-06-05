import streamlit as st
from qa_chain import get_qa_chain

st.title("Smart Legal Assistant: Indian Land Law")
st.write("Ask any question about Indian land law. Sources will be cited.")

query = st.text_input("Enter your legal question:")
if query:
    qa = get_qa_chain()
    result = qa(query)
    st.write("**Answer:**", result['result'])
    st.write("**Sources:**")
    for doc in result['source_documents']:
        st.write(f"- {doc.metadata.get('source', 'Unknown Source')}, Page: {doc.metadata.get('page', 'N/A')}") 