from fastapi import APIRouter, HTTPException, Depends
from app.models import PetPreference
from app.database import preferences_collection
from app.auth import JWTBearer

router = APIRouter(prefix="/api/v1/pet-preferences", tags=["pet-preferences"])

# Crear preferencias para una mascota
@router.post("/", dependencies=[Depends(JWTBearer())])
def create_preferences(pref: PetPreference):
    if preferences_collection.find_one({"_id": pref.id}):
        raise HTTPException(status_code=400, detail="Preferences already exist.")
    preferences_collection.insert_one(pref.dict(by_alias=True))
    return {
        "message": "Preferences created",
        "data": pref.dict(by_alias=True)
    }

# Obtener preferencias por ID de mascota (sin auth)
@router.get("/{_id}")
def get_preferences(_id: str):
    pref = preferences_collection.find_one({"_id": _id}, {"_id": 0})
    if not pref:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return pref

# Actualizar preferencias por ID de mascota
@router.put("/{_id}", dependencies=[Depends(JWTBearer())])
def update_preferences(_id: str, pref: PetPreference):
    result = preferences_collection.update_one(
        {"_id": _id},
        {"$set": {"preferences": pref.preferences}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return {"message": "Preferences updated"}

# Eliminar preferencias por ID de mascota
@router.delete("/{_id}", dependencies=[Depends(JWTBearer())])
def delete_preferences(_id: str):
    result = preferences_collection.delete_one({"_id": _id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Preferences not found.")
    return {"message": "Preferences deleted"}
