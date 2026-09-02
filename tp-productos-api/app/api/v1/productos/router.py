from fastapi import APIRouter, HTTPException, status

from app.api.v1.productos import repository
from app.api.v1.productos.schemas import ProductoCreate, ProductoResponse, ProductoUpdate

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("", response_model=list[ProductoResponse])
def listar_productos(query: str | None = None, categoria_id: int | None = None):
    return repository.list_productos(query=query, categoria_id=categoria_id)


@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int):
    producto = repository.get_by_id(producto_id)
    if producto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El producto {producto_id} no existe")
    return producto


@router.post("", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(data: ProductoCreate):
    ok, mensaje = repository.ensure_categoria(data.categoria_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=mensaje)
    return repository.create(data)


@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(producto_id: int, data: ProductoUpdate):
    if data.categoria_id is not None:
        ok, mensaje = repository.ensure_categoria(data.categoria_id)
        if not ok:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=mensaje)
    producto = repository.update(producto_id, data)
    if producto is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El producto {producto_id} no existe")
    return producto


@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int):
    eliminado = repository.delete(producto_id)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"El producto {producto_id} no existe")
