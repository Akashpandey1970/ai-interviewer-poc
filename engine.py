# engine.py

import os
import json
import time
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT, EVAL_SYSTEM_PROMPT, JSON_SCHEMA

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def get_client():
    if not client:
        raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")
    return client

def call_scenario_engine(input_data):
    """Executes structured scenario generation with automated 503 retry logic."""
    _client = get_client()
    prompt = f"Compile structured workplace conflict metrics. Difficulty Context: {input_data.get('difficulty', 'Medium')}\nPayload:\n{json.dumps(input_data, indent=2)}"
    
    max_retries = 3
    backoff_delay = 1
    
    for attempt in range(max_retries):
        try:
            response = _client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.1,
                    response_mime_type="application/json",
                    response_schema=JSON_SCHEMA
                )
            )
            return json.loads(response.text)
        except Exception as e:
            if "503" in str(e) and attempt < max_retries - 1:
                time.sleep(backoff_delay)
                backoff_delay *= 2
                continue
            raise e

def evaluate_interview_response(scenario_data, user_transcript):
    """Evaluates user transcript and returns structured scoring analytics."""
    _client = get_client()
    eval_payload = {
        "context_scenario": scenario_data,
        "captured_user_response": user_transcript
    }
    prompt = f"Analyze response and output raw analytics metrics JSON:\n{json.dumps(eval_payload, indent=2)}"
    
    response = _client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=EVAL_SYSTEM_PROMPT,
            temperature=0.2,
            response_mime_type="application/json"
        )
    )
    return json.loads(response.text)