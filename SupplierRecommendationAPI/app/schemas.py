from pydantic import BaseModel


class ProveedorResponse(BaseModel):
    Ranking: int
    Proveedor: str
    Precio_Unitario: float
    Dias_Entrega: int
    Score_Proveedor: float
    IRP: float


class RecomendacionResponse(BaseModel):
    success: bool
    producto: str
    categoria: str
    total_proveedores: int
    ranking: list[ProveedorResponse]