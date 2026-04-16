from utils.groq_client import call_model
from prompts.explanation_prompt import explanation_prompt

def explanation_chain(inputs):
    try:
        score = inputs.get("score")
        matching_data = inputs.get("matching_data")

        if score is None or matching_data is None:
            raise ValueError("Missing required inputs: 'score' or 'matching_data'")

        prompt = explanation_prompt.format(
            score=score,
            matching_data=matching_data
        )

        response = call_model(prompt)
        return response

    except Exception as e:
        return f"Error in explanation_chain: {str(e)}"