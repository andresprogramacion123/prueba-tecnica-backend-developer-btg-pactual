from pydantic import BaseModel
from enum import Enum

class categoriafondo(str,Enum):
    fpv = "FPV"
    fic = "FIC"
 
class FondoBase(BaseModel):
    id: int
    nombre: str
    monto_minimo: int
    categoria: categoriafondo