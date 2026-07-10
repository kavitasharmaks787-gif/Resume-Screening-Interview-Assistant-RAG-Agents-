
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
 
upload_file=PyMuPDFLoader("C:\\Users\\shell\\WPS Cloud Files\\165338913\\Shelly Sharma(resume).pdf")
def load_resume():
    loader=PyMuPDFLoader("C:\\Users\\shell\\WPS Cloud Files\\165338913\\Shelly Sharma(resume).pdf")
    docs=loader.load()
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks=splitter.split_documents(docs)
    return chunks
