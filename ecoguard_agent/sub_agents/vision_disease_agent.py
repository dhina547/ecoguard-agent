import json
import re
from typing import Dict

from PIL import Image
import google.generativeai as genai

from ecoguard_agent.config import MODEL_NAME


class VisionDiseaseAgent:
    """Gemini vision agent that inspects a plant leaf image for disease symptoms."""

    def __init__(self, model_name: str = MODEL_NAME) -> None:
        self.model = genai.GenerativeModel(model_name)

    def _parse_json(self, raw_text: str) -> Dict:
        match = re.search(r"{.*}", raw_text, re.S)
        if not match:
            return {
                "status": "Unknown",
                "disease_name": "Unknown",
                "confidence": 0.0,
                "visual_symptoms": "Could not parse Gemini response as JSON.",
            }
        try:
            return json.loads(match.group())
        except Exception:
            return {
                "status": "Unknown",
                "disease_name": "Unknown",
                "confidence": 0.0,
                "visual_symptoms": "JSON parsing error from Gemini response.",
            }

    def analyze(self, image_path: str) -> Dict:
        image = Image.open(image_path)

        prompt = """
        You are an agricultural plant pathologist.
        Look at the plant leaf image and return ONLY valid JSON in this schema:

        {
          "status": "Healthy or Diseased",
          "disease_name": "short name or Unknown",
          "confidence": 0.0,
          "visual_symptoms": "one sentence description"
        }
        """
        response = self.model.generate_content([prompt, image])
        raw_text = response.text or ""
        return self._parse_json(raw_text)
