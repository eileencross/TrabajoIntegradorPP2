from dataclasses import dataclass


@dataclass
class Categoria:
    id: int
    nombre: str

tp-productos-api/app/models/producto.py:
from dataclasses import dataclass


@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int
    categoria_id: int
    activo: bool = True

.gitignore (en la raíz del repo, no dentro de tp-productos-api/... pero fijate que en tu caso el .gitignore real está en tp-productos-api/.gitignore, así que ese):
venv/

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int
    categoria_id: int
    activo: bool = True