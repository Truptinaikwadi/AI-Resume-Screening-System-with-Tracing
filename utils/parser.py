import json

def safe_json_load(text):
    try:
        return json.loads(text)
    except:
        # find JSON inside text
        start = text.find("{")
        end = text.rfind("}") + 1

        if start != -1 and end != -1:
            return json.loads(text[start:end])

        return {"error": "Invalid JSON from AI"}