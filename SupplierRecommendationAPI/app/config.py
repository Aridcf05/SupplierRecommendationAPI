from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

PROVEEDORES_FILE = DATA_DIR / "proveedores.csv"
PRODUCTOS_FILE = DATA_DIR / "productos.csv"