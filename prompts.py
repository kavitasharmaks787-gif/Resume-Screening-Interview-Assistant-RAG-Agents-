skill_prompt="""Extract all skills from resume
categorize into :
1. programming language 
2.frameworks
3.databases
4.tools
5.soft skills 

resume:{context}"""

ranking_prompt="""job description
{jd}
resume:{context}
provide:
1.Match score(0-100)
2.Matching skills
3.Missing skills
4.Recommendation
"""

Interview_prompt="""Generate:
5 techniqal questions
3 practical questions
2 HR question
resume:{context}
"""

gap_analysis_prompt="""compare job description and resume
job description:{jd}

resume:{context} 

provide:

1.Missing skills
2.Missing experience
3.Learning suggestions
4.Readiness score
"""