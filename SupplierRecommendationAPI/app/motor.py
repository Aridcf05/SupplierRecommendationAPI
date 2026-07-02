from app.data import cargar_proveedores, cargar_productos

def recomendar_proveedores(solicitud):

    print("\n===== SOLICITUD RECIBIDA =====")
    print(solicitud)

    proveedores = cargar_proveedores()
    productos = cargar_productos()

    producto = productos[productos["Nombre Producto"] == solicitud.producto]

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
    
    precio_score = (
        evaluacion["Precio Unitario"].max() -
        evaluacion["Precio Unitario"]
    ) / (
        evaluacion["Precio Unitario"].max() -
        evaluacion["Precio Unitario"].min()
    )

    tiempo_score = (
        evaluacion["Dias Entrega"].max() -
        evaluacion["Dias Entrega"]
    ) / (
        evaluacion["Dias Entrega"].max() -
        evaluacion["Dias Entrega"].min()
    )

    evaluacion["Score_Proveedor"] = (
        precio_score * 0.60 +
        tiempo_score * 0.40
    )

    precio_norm = (
        evaluacion["Precio Unitario"].max() -
        evaluacion["Precio Unitario"]
    ) / (
        evaluacion["Precio Unitario"].max() -
        evaluacion["Precio Unitario"].min()
    )

    tiempo_norm = (
        evaluacion["Dias Entrega"].max() -
        evaluacion["Dias Entrega"]
    ) / (
        evaluacion["Dias Entrega"].max() -
        evaluacion["Dias Entrega"].min()
    )

    evaluacion["IRP"] = (
        evaluacion["Score_Proveedor"] * 0.60 +
        precio_norm * 0.25 +
        tiempo_norm * 0.15
    )


    evaluacion = evaluacion.sort_values(
        by="IRP",
        ascending=False
    ).reset_index(drop=True)

    evaluacion["Ranking"] = evaluacion.index + 1

    top3 = evaluacion.head(3)

    return {
    "success": True,
    "producto": solicitud.producto,
    "categoria": categoria,
    "ranking": top3.to_dict(orient="records")
}