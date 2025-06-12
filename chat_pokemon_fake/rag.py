from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

print("API key:", os.getenv("GEMINI_API_KEY"))

def carregar_base_conhecimento():
    loader = TextLoader("arquivos/pokemon_fake.txt", encoding="utf-8")
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_split = splitter.split_documents(docs)
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GEMINI_API_KEY"))
    vectordb = FAISS.from_documents(docs_split, embedding)
    return vectordb

def buscar_contexto(pergunta, vectordb):
    docs = vectordb.similarity_search(pergunta, k=3)
    return "\\n".join([doc.page_content for doc in docs])
