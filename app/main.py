from fastapi import FastAPI
from app.routers import fondos

app = FastAPI()

@app.get("/")
def hola_mundo():
    return {"Hola": "Mundo"}

#Incluimos routers
app.include_router(fondos.router)