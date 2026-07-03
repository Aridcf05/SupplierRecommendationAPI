from app.data import obtener_proveedores, obtener_productos
from app.services import (
    calcular_score,
    calcular_irp,
    generar_ranking
)
from app.logger import logger


def recomendar_proveedores(solicitud):

    logger.info("========================================")
    logger.info("Nueva solicitud recibida")
    logger.info(f"Producto: {solicitud.producto}")
    logger.info(f"Cantidad: {solicitud.cantidad}")
    logger.info(f"Ciudad: {solicitud.ciudad}")
    logger.info(f"Presupuesto: {solicitud.presupuesto}")
    logger.info("========================================")

    proveedores = obtener_proveedores()
    productos = obtener_productos()

    producto = productos[
        productos["Nombre Producto"] == solicitud.producto
    ]

    if producto.empty:

        logger.warning(
            f"Producto '{solicitud.producto}' no encontrado."
        )

        return {
            "success": False,
            "mensaje": "Producto no encontrado"
        }

    categoria = producto.iloc[0]["Categoria"]

    logger.info(f"Categoría encontrada: {categoria}")

    proveedores_filtrados = proveedores[
        proveedores["Categoria"] == categoria
    ]

    logger.info(
        f"Proveedores encontrados: {len(proveedores_filtrados)}"
    )

    evaluacion = proveedores_filtrados.copy()

    # ==============================
    # MOTOR INTELIGENTE
    # ==============================

    logger.info("Calculando Score...")

    evaluacion = calcular_score(evaluacion)

    logger.info("Calculando IRP...")

    evaluacion = calcular_irp(evaluacion)

    logger.info("Generando ranking...")

    top3 = generar_ranking(evaluacion)

    logger.info("Ranking generado correctamente.")

    return {
        "success": True,
        "producto": solicitud.producto,
        "categoria": categoria,
        "total_proveedores": len(top3),
        "ranking": top3.to_dict(orient="records")
    }