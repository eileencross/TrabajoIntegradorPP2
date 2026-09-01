from app.models.categoria import Categoria
from app.models.producto import Producto

categorias: list[Categoria] = [
    Categoria(id=1, nombre="Electrónica"),
    Categoria(id=2, nombre="Hogar"),
    Categoria(id=3, nombre="Librería"),
]

productos: list[Producto] = [
    Producto(id=1, nombre="Notebook Lenovo", precio=850000.0, stock=5, categoria_id=1),
    Producto(id=2, nombre="Auriculares Bluetooth", precio=35000.0, stock=20, categoria_id=1),
    Producto(id=3, nombre="Cafetera eléctrica", precio=42000.0, stock=8, categoria_id=2),
    Producto(id=4, nombre="Juego de sábanas", precio=18000.0, stock=15, categoria_id=2),
    Producto(id=5, nombre="Cuaderno universitario", precio=3500.0, stock=50, categoria_id=3),
    Producto(id=6, nombre="Lapicera Bic x3", precio=1200.0, stock=100, categoria_id=3),
]