import json

from google import genai
from decouple import config

client = genai.Client(api_key=config('GEMINI_API_KEY'))

MODEL_NAME = 'gemini-flash-latest'


def explain_medical_text(diagnosis_or_notes):
    """
    Takes doctor's diagnosis/notes and returns a patient-friendly explanation.
    """
    prompt = f"""
You are a medical assistant helping patients understand their diagnosis.
Explain the following medical information in simple, non-technical language
that a patient with no medical background can understand.
Keep it to 3-4 short sentences. Do not give new medical advice, only explain
what is already written.

Medical text: {diagnosis_or_notes}

Respond with plain text only, no markdown formatting.
"""
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Could not generate explanation right now. ({str(e)})"


def check_symptoms(symptom_text):
    """
    Takes patient-described symptoms and returns possible causes + urgency level.
    Returns a dict: {"causes": str, "urgency": "mild"|"moderate"|"urgent"}
    """
    prompt = f"""
A patient describes these symptoms: "{symptom_text}"

Provide a brief, cautious response as JSON with exactly these keys:
- "causes": 2-3 possible general causes (plain language, 2-3 sentences max)
- "urgency": one of "mild", "moderate", or "urgent"

Always include a note that this is not a diagnosis and a doctor should be consulted.
Respond with ONLY valid JSON, no markdown code fences, no extra text.

Example format:
{{"causes": "This could be due to X or Y. It is not a diagnosis.", "urgency": "mild"}}
"""
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        text = response.text.strip()
        text = text.replace('```json', '').replace('```', '').strip()

        data = json.loads(text)
        return {
            'causes': data.get('causes', 'Unable to determine possible causes.'),
            'urgency': data.get('urgency', 'moderate'),
        }
    except Exception as e:
        return {
            'causes': f'Could not analyze symptoms right now. Please consult a doctor. ({str(e)})',
            'urgency': 'moderate',
        }