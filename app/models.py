from typing import Dict
from pydantic import BaseModel, Field

class PetPreference(BaseModel):
    id: str = Field(..., alias="_id")
    preferences: Dict[str, str]

    class Config:
        allow_population_by_field_name = True
