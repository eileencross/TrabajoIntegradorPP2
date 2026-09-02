from fastapi import FastAPI

from app.api.v1.productos.router import router as productos_router

app = FastAPI(
    title="TP Productos API",
    description="API REST de catalogo de productos con arquitectura de capas.",
)


@app.get("/")
def bienvenida():
    return {"mensaje": "Bienvenido a la API de Productos"}


app.include_router(productos_router)
