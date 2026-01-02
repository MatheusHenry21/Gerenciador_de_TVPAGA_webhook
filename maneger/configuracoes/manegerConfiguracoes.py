
from data.dao.utilDAO import excluir_bancos_efetivos_testes, existencia_ambos_clientes

def resetar_banco():
    situacao = existencia_ambos_clientes()
    if not situacao:
        return []
    excluir_bancos_efetivos_testes()
    return "Sistema resetado com sucesso!"