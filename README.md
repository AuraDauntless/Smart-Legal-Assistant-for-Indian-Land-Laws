# Smart-Legal-Assistant-for-Indian-Land-Laws

A domain-specific AI chatbot for Indian land law that:
- Accepts Indian land law PDFs
- Embeds them into a vector database
- Uses GPT to answer queries accurately
- Cites sources — no hallucinations!

## Tech Stack
- LangChain (PyPDFLoader, RetrievalQA, etc.)
- OpenAI (text-embedding-ada-002, gpt-3.5-turbo)
- ChromaDB (local vector database)
- Streamlit (frontend)

## Setup
1. Clone/download this folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   ```
4. Place your PDF (e.g., `land_laws.pdf`) in this directory.
5. Ingest the PDF:
   ```bash
   python ingest.py
   ```
6. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Enter your legal question in the Streamlit UI.
- The assistant will answer and cite the relevant sources from the PDF.

---
**Note:**
- Only answers based on the ingested PDF (no hallucinations).
- You can replace `land_laws.pdf` with any other Indian land law PDF. 
