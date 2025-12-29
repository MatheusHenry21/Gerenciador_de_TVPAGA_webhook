
from maneger.gestaoCliente.manegerGestaoCliente import(
    listar_clientes_efetivos,
    listar_clientes_testes
)

from fastapi import APIRouter

router = APIRouter()

@router.get("/efetivos")
def listar_efetivos_router():
    return {"Clientes efetivos": listar_clientes_efetivos()}

@router.get("/testes")
def listar_testes_router():
    return {"Clientes testes": listar_clientes_testes()}