
from moldels.moldeContato import info_clientes_vencendo
from maneger.relatorio.manegerRelatorio import (
    quantidade_efetivos,
    quantidade_testes,
    quantidade_total,
    tempo_para_cobrança
    )

def main_relatorio(phone, text):
    pass

def total_clientes():
    return {"total": quantidade_total()}

def total_clientes_efetivos():
    return {"total_efetivos": quantidade_efetivos()}

def total_clientes_testes():
    return {"total_testes": quantidade_testes()}

def clientes_preste_vencer():
    return {"clientes a vencer": info_clientes_vencendo(tempo_para_cobrança())}