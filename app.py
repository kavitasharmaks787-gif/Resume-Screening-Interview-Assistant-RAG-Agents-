import streamlit as st 
from parser import load_resume
from emb import get_embeddings
from vect import create_vectorestore
from llm import get_llm
from anay import (extract_skills,rank_candidate,generate_Interview_questions,analyze_gap)
from langchain_groq import ChatGroq
from dotenv import load_dotenv
# from embeddings import embeddings

load_dotenv()



st.title("Resume Screening & Interview Assistant👩‍💻")
# resume=st.file_uploader()
resume=st.file_uploader("upload resume")
query=st.text_input("Ask Questions")
jd=st.text_area("paste job description")
task=st.selectbox("choose task",[
    "skills extraction",
    "candidate ranking",
    "interview questions",
    "gap analysis"
])
result=""
# task=st.selectbox("choose task",["skills extraction","candidate ranking","interview questions","gap analysis"])
if resume:
    with open("C:\\Users\\shell\\WPS Cloud Files\\165338913\\Shelly Sharma(resume).pdf","wb") as f:
        f.write(resume.getbuffer())
    chunks=load_resume()
    embeddings=get_embeddings
    # db=create_vectorestore(chunks,embeddings)
    db =create_vectorestore(chunks, embeddings())
    llm=get_llm()
    # if st.button("General Answer"):
    #      if query=="":
    #         st.warning("Enter Your Question")
    if st.button("Analyze"):
        if task=="skills extraction":
            result=extract_skills(db,llm)
        elif task=="candidate ranking":
            result=rank_candidate(db,llm,jd)
        elif task=="interview questions":
            result=generate_Interview_questions(db,llm)
        elif task=="gap analysis":
            result=analyze_gap(db,llm,jd)
        
    if result:
        st.markdown(result)
        st.write(result)
    if st.button("General Answer"): 
        if query=="":
            st.warning("Enter Your Question")
        else:
           response=llm.invoke(query)
           
        print(response.content)
        st.write(response.content)
        st.success("Successfully completed")
        print(result)


       
