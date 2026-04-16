from utils.groq_client import call_model
from prompts.scoring_prompt import scoring_prompt
from utils.parser import safe_json_load

def scoring_chain(matching_data):
    prompt = scoring_prompt.format(matching_data=matching_data)
    response = call_model(prompt)

    return safe_json_load(response)