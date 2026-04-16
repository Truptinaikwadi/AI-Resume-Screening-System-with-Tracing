from langchain_core.prompts import PromptTemplate
matching_prompt = PromptTemplate.from_template("""
You are a resume-job matching system.

STRICT RULES:
- Compare ONLY given data
- Do NOT hallucinate missing skills
- Output MUST be valid JSON ONLY

Return format:

{{
  "matching_skills": [],
  "missing_skills": [],
  "experience_match": "",
  "tools_match": []
}}

Job Description:
{job}

Resume Data:
{resume_data}
""")