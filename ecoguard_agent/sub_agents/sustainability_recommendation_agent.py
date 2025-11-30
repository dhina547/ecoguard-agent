from typing import Dict

import google.generativeai as genai

from ecoguard_agent.config import MODEL_NAME


class SustainabilityRecommendationAgent:
    """Gemini agent that suggests sustainable treatment & prevention steps."""

    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self.model = genai.GenerativeModel(model_name)

    def generate(self, disease_info: Dict, climate_info: Dict, location: str = "Unknown") -> str:
        prompt = f"""
        You are an agricultural sustainability expert helping a small farmer.

        Disease info: {disease_info}
        Climate info: {climate_info}
        Location (rough): {location}

        TASK:
        1. If the leaf appears healthy, give only short preventive advice.
        2. If diseased, give:
           - 2–3 sustainable / organic treatment steps.
           - 2–3 preventive measures for future.
        3. Use simple, farmer-friendly language.
        4. Use bullet points.
        5. Do not mention that you are an AI model.

        Answer in plain text.
        """
        response = self.model.generate_content(prompt)
        return response.text or "No recommendation generated."
