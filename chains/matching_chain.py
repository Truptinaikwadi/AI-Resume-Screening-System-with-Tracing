from utils.groq_client import call_model
from prompts.matching_prompt import matching_prompt
from utils.parser import safe_json_load

def matching_chain(job, resume_data):
    prompt = matching_prompt.format(job=job, resume_data=resume_data)
    response = call_model(prompt)

    return safe_json_load(response)