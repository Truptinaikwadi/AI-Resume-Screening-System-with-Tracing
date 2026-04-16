from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate.from_template("""
You are a resume information extractor.

Extract ONLY from given text.

Return ONLY valid JSON. No explanation.

{{
  "skills": [],
  "experience": "",
  "tools": []
}}

Resume:
{resume}
""")