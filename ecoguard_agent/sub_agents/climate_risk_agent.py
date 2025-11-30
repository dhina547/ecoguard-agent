from typing import Dict, List


class ClimateRiskAgent:
    """Rule-based climate risk analyzer for crop disease context."""

    def evaluate(self, disease_info: Dict, humidity: float, temperature: float) -> Dict:
        risks: List[str] = []

        if humidity > 70:
            risks.append("High humidity can accelerate fungal and bacterial disease spread.")
        if temperature > 32:
            risks.append("High temperature may increase plant stress and weaken disease resistance.")
        if temperature < 15:
            risks.append("Low temperature might stress certain crops and modify disease dynamics.")

        if not risks:
            risks.append("No major climate-related risk factors detected from humidity and temperature.")

        return {
            "disease": disease_info.get("disease_name", "Unknown"),
            "humidity": humidity,
            "temperature": temperature,
            "risks": risks,
        }
