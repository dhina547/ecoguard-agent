from ecoguard_agent.sub_agents.vision_disease_agent import VisionDiseaseAgent
from ecoguard_agent.sub_agents.climate_risk_agent import ClimateRiskAgent
from ecoguard_agent.sub_agents.sustainability_recommendation_agent import SustainabilityRecommendationAgent
from ecoguard_agent.memory import MemoryAgent


class EcoGuardAgent:
    """
    Orchestrates the full EcoGuard multi-agent pipeline:

    1. VisionDiseaseAgent -> detect disease from leaf image
    2. ClimateRiskAgent   -> reason about humidity & temperature
    3. SustainabilityRecommendationAgent -> generate eco-friendly advice
    4. MemoryAgent        -> store case for later inspection
    """
    def __init__(self):
        self.vision = VisionDiseaseAgent()
        self.climate = ClimateRiskAgent()
        self.recommender = SustainabilityRecommendationAgent()
        self.memory = MemoryAgent()

    def run(self, image_path: str, humidity: float, temperature: float, location: str = "Unknown"):
        """Run the full pipeline and return a combined result dict."""
        disease = self.vision.analyze(image_path=image_path)
        climate = self.climate.evaluate(disease_info=disease, humidity=humidity, temperature=temperature)
        recommendation = self.recommender.generate(disease_info=disease, climate_info=climate, location=location)

        self.memory.store(
            image_path=image_path,
            disease_info=disease,
            climate_info=climate,
            recommendation=recommendation,
        )

        return {
            "disease": disease,
            "climate": climate,
            "recommendation": recommendation,
        }
