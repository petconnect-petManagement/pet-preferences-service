from fastapi import APIRouter, HTTPException
from app.models import PetPreference
from app.database import preferences_collection

router = APIRouter(prefix="/api/v1/pet-preferences", tags=["pet-preferences"])

# Crear preferencias para una mascota
@router.post("/")
def create_preferences(pref: PetPreference):
    if preferences_collection.find_one({"_id": pref._id}):
        raise HTTPException(status_code=400, detail="Preferences already exist.")

    preferences_collection.insert_one(pref.dict())
    return {
        "message": "Preferences created",
        "data": pref.dict()
    }

# Obtener preferencias por ID de mascota
@router.get("/{_id}")
def get_preferences(_id: str):
    pref = preferences_collection.find_one({"_id": _id}, {"_id": 0})
    if not pref:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return pref

# Actualizar preferencias por ID de mascota
@router.put("/{_id}")
def update_preferences(_id: str, pref: PetPreference):
    result = preferences_collection.update_one(
        {"_id": _id},
        {"$set": {"preferences": pref.preferences}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return {"message": "Preferences updated"}

# Eliminar preferencias por ID de mascota
@router.delete("/{_id}")
def delete_preferences(_id: str):
    result = preferences_collection.delete_one({"_id": _id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return {"message": "Preferences deleted"}
