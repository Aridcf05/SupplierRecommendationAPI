from app.data import obtener_proveedores, obtener_productos
from app.services import (
    calcular_score,
    calcular_irp,
    generar_ranking
)


def recomendar_proveedores(solicitud):

    print("\n===== SOLICITUD RECIBIDA =====")
    print(solicitud)

    
    proveedores = obtener_proveedores()
    productos = obtener_productos()

    producto = productos[
        productos["Nombre Producto"] == solicitud.producto
    ]

    if producto.empty:
        return {
            "success": False,
            "mensaje": "Producto no encontrado"
        }

    categoria = producto.iloc[0]["Categoria"]

    proveedores_filtrados = proveedores[
        proveedores["Categoria"] == categoria
    ]

    evaluacion = proveedores_filtrados.copy()

    # ==============================
    # MOTOR INTELIGENTE
    # ==============================

    evaluacion = calcular_score(evaluacion)

    evaluacion = calcular_irp(evaluacion)

    top3 = generar_ranking(evaluacion)

    return {
        "success": True,
        "producto": solicitud.producto,
        "categoria": categoria,
        "total_proveedores": len(top3),
        "ranking": top3.to_dict(orient="records")
    }