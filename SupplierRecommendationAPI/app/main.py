from app.models import Solicitud
from app.motor import recomendar_proveedores
from app.schemas import RecomendacionResponse
from fastapi import FastAPI, HTTPException
from app.logger import logger

app = FastAPI(
    title="Supplier Recommendation API",
    version="1.0.0",
    description="Sistema Inteligente de Selección de Proveedores",
    openapi_version="3.0.3"
)

@app.get("/")
def home():
    return {
        "status": "OK",
        "message": "Supplier Recommendation API funcionando correctamente"
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Supplier Recommendation API"
    }

@app.post(
    "/recomendar",
    response_model=RecomendacionResponse
)
def recomendar(solicitud: Solicitud):

    try:

        ranking = recomendar_proveedores(solicitud)

        if ranking.get("success") is False:
            raise HTTPException(
                status_code=404,
                detail=ranking["mensaje"]
            )

        return ranking

    except HTTPException:
        raise

    except Exception as e:

        logger.exception("Error interno en la recomendación.")

        raise HTTPException(
            status_code=500,
            detail="Error interno del servidor."
        )