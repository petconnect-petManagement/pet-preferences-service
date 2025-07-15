from typing import Dict
from pydantic import BaseModel, Field

class PetPreference(BaseModel):
    id: str = Field(..., alias="_id")
    preferences: Dict[str, str]

    model_config = {
        "populate_by_name": True  # reemplazo de allow_population_by_field_name
    }
