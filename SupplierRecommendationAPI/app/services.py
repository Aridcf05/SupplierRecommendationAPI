from app.constants import (
    PESO_PRECIO,
    PESO_TIEMPO,
    PESO_SCORE,
    PESO_PRECIO_IRP,
    PESO_TIEMPO_IRP
)


def calcular_score(evaluacion):

    precio_min = evaluacion["Precio Unitario"].min()
    precio_max = evaluacion["Precio Unitario"].max()

    dias_min = evaluacion["Dias Entrega"].min()
    dias_max = evaluacion["Dias Entrega"].max()

    # Evitar división por cero
    if precio_max == precio_min:
        evaluacion["Precio_Score"] = 1
    else:
        evaluacion["Precio_Score"] = (
            precio_max - evaluacion["Precio Unitario"]
        ) / (precio_max - precio_min)

    if dias_max == dias_min:
        evaluacion["Tiempo_Score"] = 1
    else:
        evaluacion["Tiempo_Score"] = (
            dias_max - evaluacion["Dias Entrega"]
        ) / (dias_max - dias_min)

    evaluacion["Score_Proveedor"] = (
        evaluacion["Precio_Score"] * PESO_PRECIO +
        evaluacion["Tiempo_Score"] * PESO_TIEMPO
    )

    return evaluacion


def calcular_irp(evaluacion):

    evaluacion["IRP"] = (
        evaluacion["Score_Proveedor"] * PESO_SCORE +
        evaluacion["Precio_Score"] * PESO_PRECIO_IRP +
        evaluacion["Tiempo_Score"] * PESO_TIEMPO_IRP
    )

    return evaluacion


def generar_ranking(evaluacion):

    evaluacion = evaluacion.sort_values(
        by="IRP",
        ascending=False
    ).reset_index(drop=True)

    evaluacion["Ranking"] = evaluacion.index + 1

    top3 = evaluacion.head(3)

    return top3