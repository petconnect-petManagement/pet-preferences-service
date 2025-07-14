from typing import Optional, Dict
from pydantic import BaseModel

class PetPreference(BaseModel):
    _id: str
    preferences: Dict[str, str]  
