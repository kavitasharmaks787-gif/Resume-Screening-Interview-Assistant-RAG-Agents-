from prompts import (skill_prompt,ranking_prompt,Interview_prompt,gap_analysis_prompt)


def extract_skills(db,llm):
    docs=db.similarity_search("technial skills programming languages frameworks ",k=5)
    context="\n".join([doc.page_content for doc in docs])
    prompt=skill_prompt.format(context=context)
    response=llm.invoke(prompt)
    return response.content
def rank_candidate(db,llm,jd):
    docs=db.similarity_search(jd,k=5)
    context="\n".join([doc.page_content for doc in docs])
    prompt=ranking_prompt.format(jd=jd,context=context)
    response=llm.invoke(prompt)
    return response.content
def generate_Interview_questions(db,llm):
    docs=db.similarity_search("projects experience achivements",k=5)
    context="\n".join([doc.page_content for doc in docs])
    prompt=Interview_prompt.format(context=context)
    response=llm.invoke(prompt)
    return response.content
def analyze_gap(db,llm,jd):
    docs=db.similarity_search(jd,k=5)
    context="\n".join([doc.page_content for doc in docs])
    prompt=gap_analysis_prompt.format(jd=jd,context=context)
    response=llm.invoke(prompt)
    return response.content
