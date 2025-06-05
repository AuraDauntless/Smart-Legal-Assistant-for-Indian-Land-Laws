from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os

# Load PDF
def ingest_pdf(pdf_path, persist_directory="chroma_db"):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    db = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    db.persist()
    print(f"Ingested and stored embeddings for {pdf_path} in {persist_directory}")

if __name__ == "__main__":
    ingest_pdf("land_laws.pdf") 