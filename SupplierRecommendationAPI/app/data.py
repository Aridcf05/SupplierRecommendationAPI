import pandas as pd

from app.config import (
    PROVEEDORES_FILE,
    PRODUCTOS_FILE
)

def cargar_proveedores():

    return pd.read_csv(PROVEEDORES_FILE)

def cargar_productos():

    return pd.read_csv(PRODUCTOS_FILE)