# run_agent.py
from ecoguard_agent.agent import EcoGuardAgent

agent = EcoGuardAgent()

result = agent.run(
    image_path="images_leaf.jpeg",  # put any leaf image here
    humidity=78.0,
    temperature=29.0,
    location="Tamil Nadu, India"
)

print("\n Disease Info:")
print(result["disease"])

print("\n Climate Info:")
print(result["climate"])

print("\n Sustainable Recommendation:")
print(result["recommendation"])
