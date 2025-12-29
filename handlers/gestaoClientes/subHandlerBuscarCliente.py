
from maneger.exceptions.exceptions_routers import DadosExistenteError
from maneger.gestaoCliente.manegerGestaoCliente import(
    buscar_por_nome_efetivo,
    buscar_por_nome_teste,
    buscar_celular,
    buscar_id_efetivo,
    buscar_id_teste
)

from fastapi import (
    APIRouter,
    HTTPException,
    Query
    )

router = APIRouter()

#####################################################################################

def error_existencia(e):
    raise HTTPException(
            status_code=404,
            detail=str(e)
        )

#####################################################################################

@router.get("/buscar_nome_efetivo")
def buscar_por_nome_cliente_efetivo(nome: str = Query(...)):
    try:
        return {"Cliente": buscar_por_nome_efetivo(nome)}
    except DadosExistenteError as e:
        error_existencia(e)

@router.get("/buscar_nome_teste")
def buscar_por_nome_cliente_teste(nome: str = Query(...)):
    try:
        return {"Cliente": buscar_por_nome_teste(nome)}
    except DadosExistenteError as e:
        error_existencia(e)

#####################################################################################

@router.get("/buscar_por_celular")
def buscar_por_celular_cliente(celular: int = Query(
        ...,
        ge=1_000_000_000,
        le=99_999_999_999
    )):
    try:
        return {"Cliente": buscar_celular(celular)}
    except DadosExistenteError as e:
        error_existencia(e)

#####################################################################################

@router.get("/buscar_por_id_efetivo")
def buscar_por_id_cliente_efetivo(id: int = Query(..., ge=1)):
    try:
        return {"Cliente": buscar_id_efetivo(id)}
    except DadosExistenteError as e:
        error_existencia(e)

@router.get("/buscar_por_celular_id_testes")
def buscar_por_id_cliente_teste(id: int = Query(..., ge=1)):
    try:
        return {"Cliente": buscar_id_teste(id)}
    except DadosExistenteError as e:
        error_existencia(e)