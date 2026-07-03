import pandas as pd

from app.config import (
    PROVEEDORES_FILE,
    PRODUCTOS_FILE
)


# ==========================================
# LECTURA DESDE CSV
# ==========================================

def cargar_proveedores_csv():
    return pd.read_csv(PROVEEDORES_FILE)


def cargar_productos_csv():
    return pd.read_csv(PRODUCTOS_FILE)


# ==========================================
# PUNTO DE ENTRADA DE LA CAPA DE DATOS
# ==========================================

def obtener_proveedores():
    """
    Obtiene los proveedores desde la fuente de datos configurada.
    Actualmente utiliza archivos CSV.
    """
    return cargar_proveedores_csv()


def obtener_productos():
    """
    Obtiene los productos desde la fuente de datos configurada.
    Actualmente utiliza archivos CSV.
    """
    return cargar_productos_csv()