
from routers.gestaoClientes.subRoutersBuscarCliente import router as buscarClientes
from routers.gestaoClientes.subRoutersListarCliente import router as listarClientes
from maneger.gestaoCliente.manegerGestaoCliente import(
    cadastrar_efetivos,
    cadastrar_testes,
    atualizar_efetivo,
    atualizar_teste,
    deletar_efetivo,
    deletar_teste
)
from maneger.exceptions.exceptions_routers import (
    NumeroExistenteError,
    IdExistenteError,
    NomeVazio
    )

from typing import Optional
from fastapi import (
    APIRouter,
    HTTPException,
    Path
    )
from pydantic import (
    BaseModel,
    Field
)


router = APIRouter()

router.include_router(
    buscarClientes,
    prefix="/buscar_clientes",
    tags=["Buscar_cliente"]
)

router.include_router(
    listarClientes,
    prefix="/listas",
    tags=["Listar"]
)

class CadastrarCliente(BaseModel):
    nome: str = Field(...)
    celular: int = Field(
        ...,
        ge=1_000_000_000,
        le=99_999_999_999
    )

class AtualizarCliente(BaseModel):
    id: int = Field(..., ge=1)
    nome: Optional[str] = None
    celular: Optional[int] = Field(
        default=None,
        ge=1_000_000_000,
        le=99_999_999_999
    )

class Id(BaseModel):
    id: int = Field(..., ge=1)


#####################################################################################


def numero_existente_error(e):
    raise HTTPException(
        status_code=409,
        detail=str(e)
    )

def id_existente_error(e):
    raise HTTPException(
        status_code=404,
        detail=str(e)
    )

def nome_vazio_error(e):
    raise HTTPException(
        status_code=422,
        detail=str(e)
    )

#####################################################################################

@router.post("/cadastrar_efetivo")
def cadastrar_cliente_efetivos(informacoes: CadastrarCliente):
    try:
        return {"msg": cadastrar_efetivos(
            informacoes.nome,
            informacoes.celular
            )}
    except NumeroExistenteError as e:
        numero_existente_error(e)
    except NomeVazio as e:
        nome_vazio_error(e)


@router.post("/cadastrar_teste")
def cadastrar_cliente_teste(informacoes: CadastrarCliente):
    try:
        return {"msg": cadastrar_testes(
            informacoes.nome,
            informacoes.celular
            )}
    except NumeroExistenteError as e:
        numero_existente_error(e)
    except NomeVazio as e:
        nome_vazio_error(e)

#####################################################################################

@router.put("/atualizar_efetivo")
def atualizar_cliente_efetivo(informacoes: AtualizarCliente):
    try:
        return {"msg": atualizar_efetivo(
            informacoes.id,
            informacoes.nome,
            informacoes.celular
            )}
    except IdExistenteError as e:
        id_existente_error(e)
    except NumeroExistenteError as e:
        numero_existente_error(e)


@router.put("/atualizar_teste")
def atualizar_cliente_teste(informacoes: AtualizarCliente):
    try:
        return {"msg": atualizar_teste(
            informacoes.id,
            informacoes.nome,
            informacoes.celular
            )}
    except IdExistenteError as e:
        id_existente_error(e)
    except NumeroExistenteError as e:
        numero_existente_error(e)

#####################################################################################

@router.delete("/remover_efetivo")
def remover_cliente_efetivo(id: int = Path(..., ge=1)):
    try:
        return {"msg": deletar_efetivo(id)}
    except IdExistenteError as e:
        id_existente_error(e)

@router.delete("/remover_teste")
def remover_cliente_teste(id: int = Path(..., ge=1)):
    try:
        return {"msg": deletar_teste(id)}
    except IdExistenteError as e:
        id_existente_error(e)
    