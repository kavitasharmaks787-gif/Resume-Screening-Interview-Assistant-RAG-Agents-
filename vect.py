from langchain_community.vectorstores import FAISS

def create_vectorestore(chunks,embeddings):
    db=FAISS.from_documents(chunks,embeddings)
    return db