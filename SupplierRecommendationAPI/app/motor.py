from app.data import (
    cargar_proveedores,
    cargar_productos
)

def recomendar_proveedores(solicitud):

    proveedores = cargar_proveedores()

    productos = cargar_productos()

    print(proveedores.head())

    print(productos.head())

    return [
        {
            "mensaje": "Datos cargados correctamente"
        }
    ]