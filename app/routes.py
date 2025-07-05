from fastapi import APIRouter, HTTPException
from app.models import PetPreference
from app.database import preferences_collection

router = APIRouter(prefix="/api/v1/pet-preferences", tags=["pet-preferences"])

@router.post("/")
def create_preferences(pref: PetPreference):
    if preferences_collection.find_one({"pet_id": pref.pet_id}):
        raise HTTPException(status_code=400, detail="Preferences already exist.")
    preferences_collection.insert_one(pref.dict())
    return {"message": "Preferences created"}

@router.get("/{pet_id}")
def get_preferences(pet_id: str):
    pref = preferences_collection.find_one({"pet_id": pet_id}, {"_id": 0})
    if not pref:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return pref

@router.put("/{pet_id}")
def update_preferences(pet_id: str, pref: PetPreference):
    result = preferences_collection.update_one(
        {"pet_id": pet_id},
        {"$set": {"preferences": pref.preferences}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return {"message": "Preferences updated"}

@router.delete("/{pet_id}")
def delete_preferences(pet_id: str):
    result = preferences_collection.delete_one({"pet_id": pet_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return {"message": "Preferences deleted"}
