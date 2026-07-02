# Supplier Recommendation API

## Descripción

Supplier Recommendation API es una API REST desarrollada con FastAPI que forma parte del proyecto de tesis:

**"Sistema predictivo basado en Machine Learning para la selección de proveedores en el sector diseño de interiores de Lima Metropolitana."**

La API implementa un motor inteligente de recomendación que evalúa proveedores según criterios de negocio como precio, tiempo de entrega y categoría del producto, generando un ranking de proveedores para apoyar la toma de decisiones.

---

# Tecnologías

- Python 3.13
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Joblib
- Git
- GitHub
- Render
- Microsoft Power Platform

---

# Arquitectura

```
Power Apps
      │
      ▼
FastAPI
      │
      ▼
Motor Inteligente
      │
      ▼
Capa de Datos
      │
      ▼
Microsoft Lists (Producción)
CSV (Desarrollo)
```

---

# Estructura del Proyecto

```
SupplierRecommendationAPI/

│

├── app/

│   ├── __init__.py

│   ├── main.py

│   ├── models.py

│   ├── motor.py

│   ├── data.py

│   ├── config.py

│   └── utils.py

│

├── data/

│   ├── proveedores.csv

│   └── productos.csv

│

├── modelo/

│   ├── modelo_xgboost.pkl

│   └── label_encoders.pkl

│

├── requirements.txt

├── README.md

├── render.yaml

└── .gitignore
```

---

# Funcionalidades

- API REST para recomendación de proveedores.
- Lectura de proveedores y productos.
- Filtrado por categoría.
- Evaluación de proveedores.
- Cálculo del Score del proveedor.
- Cálculo del Índice de Recomendación del Proveedor (IRP).
- Generación del Top 3 de proveedores.
- Preparado para integración con Microsoft Lists.
- Preparado para integración con Power Apps.

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/supplier-recommendation-api.git
```

Entrar al proyecto

```bash
cd SupplierRecommendationAPI
```

Crear entorno virtual

Windows

```bash
python -m venv .venv
```

Activar entorno

```bash
.venv\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Endpoint disponible

## GET /

Verifica el estado de la API.

Respuesta

```json
{
    "status":"OK",
    "message":"Supplier Recommendation API funcionando correctamente"
}
```

---

## POST /recomendar

Recibe una solicitud de compra y devuelve un ranking de proveedores.

Ejemplo

```json
{
    "producto":"Escritorio Ejecutivo",
    "cantidad":20,
    "ciudad":"Lima",
    "presupuesto":25000
}
```

Respuesta

```json
{
    "success": true,
    "producto":"Escritorio Ejecutivo",
    "categoria":"Muebles",
    "ranking":[
        {
            "Ranking":1,
            "Proveedor":"Grupo Muebles",
            "Score_Proveedor":0.80,
            "IRP":0.73
        }
    ]
}
```

---

# Flujo del Sistema

```
Solicitud

↓

API REST

↓

Motor Inteligente

↓

Carga de Datos

↓

Evaluación de Proveedores

↓

Cálculo del Score

↓

Cálculo del IRP

↓

Ranking

↓

Top 3

↓

Respuesta JSON
```

---

# Próximas Integraciones

- Microsoft Lists
- Power Apps
- Power Automate
- Power BI
- Render
- Modelo XGBoost

---

# Estado del Proyecto

| Módulo | Estado |
|---------|--------|
| FastAPI | ✅ |
| Swagger | ✅ |
| Motor Inteligente | ✅ |
| Ranking | ✅ |
| Score del Proveedor | ✅ |
| IRP | ✅ |
| CSV | ✅ |
| Microsoft Lists | 🚧 |
| XGBoost | 🚧 |
| Render | 🚧 |
| Power Apps | 🚧 |

---

# Autor

Ariana Del Carpio

Ingeniería de Sistemas de Información

Universidad Peruana de Ciencias Aplicadas (UPC)

---

# Licencia

Proyecto desarrollado con fines académicos como parte del trabajo de investigación para optar el grado de Bachiller en Ingeniería de Sistemas de Información.


![Python](https://img.shields.io/badge/Python-3.13-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)

![Status](https://img.shields.io/badge/Status-In_Development-orange)
