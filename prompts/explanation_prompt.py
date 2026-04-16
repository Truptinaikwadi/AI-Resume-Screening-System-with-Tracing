from langchain_core.prompts import PromptTemplate
explanation_prompt = PromptTemplate.from_template("""
You are an AI explanation system.

RULES:
- Use only given data
- No hallucination
- Bullet points only

OUTPUT FORMAT:
- Short bullet points
- Explain why score was given

Score:
{score}

Matching Data:
{matching_data}
""")