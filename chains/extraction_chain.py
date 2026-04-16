from utils.groq_client import call_model
from prompts.extraction_prompt import extraction_prompt
from utils.parser import safe_json_load

def extraction_chain(resume):
    prompt = extraction_prompt.format(resume=resume)
    response = call_model(prompt)

    return safe_json_load(response)