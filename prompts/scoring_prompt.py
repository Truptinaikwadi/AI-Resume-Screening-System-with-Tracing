from langchain_core.prompts import PromptTemplate
scoring_prompt = PromptTemplate.from_template("""
You are a strict evaluation system.

RULES:
- Score must be integer only (0-100)
- Base score ONLY on provided matching data
- No explanations in output

OUTPUT FORMAT (JSON ONLY):
{{ "score": 0 }}

Scoring logic:
- Strong match → 80-100
- Medium match → 40-79
- Weak match → 0-39

Input:
{matching_data}
""")