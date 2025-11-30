from datetime import datetime
from typing import Any, Dict, List


class MemoryAgent:
    """Very simple in-memory store for recent EcoGuard runs."""

    def __init__(self) -> None:
        self.history: List[Dict[str, Any]] = []

    def store(self, image_path: str, disease_info: dict, climate_info: dict, recommendation: str) -> None:
        entry = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "image_path": image_path,
            "disease": disease_info,
            "climate": climate_info,
            "recommendation_preview": recommendation[:300],
        }
        self.history.append(entry)

    def get_recent(self, n: int = 3):
        return self.history[-n:]
