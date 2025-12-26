
from routers.gestaoClientes.routersGestaoClientes import id_existente_error
from maneger.exceptions.exceptions_routers import IdExistenteError
from maneger.gestaoAssinatura.manegerGestaoAssinatura import(
    converter_teste_para_efetivo,
    clientes_vencidos_efeti,
    clientes_vencidos_tes,
    renovar_assinatura
    )

from fastapi import APIRouter
from pydantic import (
    BaseModel,
    Field
    )

router = APIRouter()

class Id(BaseModel):
    id: int = Field(..., ge=1)



@router.get("/clientes_vencidos")
def listar_clientes_vencidos_efetivos():
    return {"Clientes": clientes_vencidos_efeti()}

def listar_clientes_vencidos_testes():
    return {"Clientes": clientes_vencidos_tes()}


@router.patch("/renovar_assinatura")
def renovar_assinatura_cliente(dados: Id):
    try:
        return {"msg": renovar_assinatura(dados.id)}
    except IdExistenteError as e:
        id_existente_error(e)

@router.patch("/converter_teste_para_efetivo")
def converter_cliente(dados: Id):
    try:
        return {"msg": converter_teste_para_efetivo(dados.id)}
    except IdExistenteError as e:
        id_existente_error(e)