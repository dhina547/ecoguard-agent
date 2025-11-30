import os
import google.generativeai as genai

MODEL_NAME = "gemini-2.5-flash-lite"

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY not found. Please set it as an environment variable.")

genai.configure(api_key=api_key)
