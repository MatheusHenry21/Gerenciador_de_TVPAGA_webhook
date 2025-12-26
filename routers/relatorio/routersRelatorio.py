
from moldels.moldeContato import info_clientes_vencendo
from maneger.relatorio.manegerRelatorio import (
    quantidade_efetivos,
    quantidade_testes,
    quantidade_total,
    tempo_para_cobrança
    )

from fastapi import APIRouter

router = APIRouter()

@router.get("/total_clientes")
def total_clientes():
    return {"total": quantidade_total()}

@router.get("/total_clientes/efetivos")
def total_clientes_efetivos():
    return {"total_efetivos": quantidade_efetivos()}

@router.get("/total_clientes/testes")
def total_clientes_testes():
    return {"total_testes": quantidade_testes()}

@router.get("/clientes_preste_vencer")
def clientes_preste_vencer():
    return {"clientes a vencer": info_clientes_vencendo(tempo_para_cobrança())}