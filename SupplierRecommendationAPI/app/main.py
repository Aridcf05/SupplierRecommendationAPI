from fastapi import FastAPI
from app.models import Solicitud
from app.motor import recomendar_proveedores

app = FastAPI(
    title="Supplier Recommendation API",
    description="Sistema Inteligente de Selección de Proveedores",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "OK",
        "message": "Supplier Recommendation API funcionando correctamente"
    }

@app.post("/recomendar")
def recomendar(solicitud: Solicitud):

    ranking = recomendar_proveedores(solicitud)

    return ranking