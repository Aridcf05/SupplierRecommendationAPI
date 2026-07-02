from fastapi import FastAPI

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