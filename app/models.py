from typing import Optional, Dict
from pydantic import BaseModel

class PetPreference(BaseModel):
    pet_id: str
    preferences: Dict[str, str]  # Por ejemplo {"food": "dry", "play": "ball"}
