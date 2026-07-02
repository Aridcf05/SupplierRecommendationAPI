from pydantic import BaseModel

class Solicitud(BaseModel):
    producto: str
    cantidad: int
    ciudad: str
    presupuesto: float
