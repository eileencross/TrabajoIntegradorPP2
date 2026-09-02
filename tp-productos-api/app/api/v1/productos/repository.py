from app.api.v1.productos.schemas import ProductoCreate, ProductoUpdate
from app.core import db
from app.core.db import bump_producto_id
from app.models.producto import Producto


def _find_categoria(categoria_id: int):
    return next((c for c in db.categorias if c.id == categoria_id), None)


def _to_dict(producto: Producto) -> dict:
    categoria = _find_categoria(producto.categoria_id)
    return {
        "id": producto.id,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "stock": producto.stock,
        "activo": producto.activo,
        "categoria": {"id": categoria.id, "nombre": categoria.nombre} if categoria else None,
    }


def search_by_nombre(query: str) -> list[Producto]:
    query_lower = query.lower()
    return [p for p in db.productos if query_lower in p.nombre.lower()]


def list_productos(query: str | None = None, categoria_id: int | None = None) -> list[dict]:
    productos = search_by_nombre(query) if query else list(db.productos)
    if categoria_id is not None:
        productos = [p for p in productos if p.categoria_id == categoria_id]
    return [_to_dict(p) for p in productos]


def get_by_id(producto_id: int) -> dict | None:
    producto = next((p for p in db.productos if p.id == producto_id), None)
    return _to_dict(producto) if producto else None


def ensure_categoria(categoria_id: int) -> tuple[bool, str]:
    if _find_categoria(categoria_id) is None:
        return False, f"La categoria {categoria_id} no existe"
    return True, ""


def create(data: ProductoCreate) -> dict:
    nuevo = Producto(
        id=bump_producto_id(),
        nombre=data.nombre,
        precio=data.precio,
        stock=data.stock,
        categoria_id=data.categoria_id,
    )
    db.productos.append(nuevo)
    return _to_dict(nuevo)


def update(producto_id: int, data: ProductoUpdate) -> dict | None:
    producto = next((p for p in db.productos if p.id == producto_id), None)
    if producto is None:
        return None
    cambios = data.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(producto, campo, valor)
    return _to_dict(producto)


def delete(producto_id: int) -> bool:
    producto = next((p for p in db.productos if p.id == producto_id), None)
    if producto is None:
        return False
    db.productos.remove(producto)
    return True