from fastapi import APIRouter
from app.schemas.fondos import FondoBase

router = APIRouter()

@router.get("/")
def hola_mundo():
    return {"Hola": "Mundo"}

@router.post("/fondo/crear")
def crear_fondo(fondo: FondoBase):
    return fondo