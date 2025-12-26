
from data.dao.efetivosDAO import quantidade_clientes_efetivos, clientes_vencendo
from data.dao.testesDAO import quantidade_clientes_testes


def quantidade_efetivos():
    return quantidade_clientes_efetivos()

def quantidade_testes():
    return quantidade_clientes_testes()

def quantidade_total():
    return (quantidade_clientes_testes()) + (quantidade_efetivos())

def tempo_para_cobrança():
    return clientes_vencendo()