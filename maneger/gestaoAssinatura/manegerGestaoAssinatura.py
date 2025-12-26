
from dateutil.relativedelta import relativedelta
from datetime import datetime

from moldels.moldeContato import TestesTransferencia
from moldels.moldeContato import info_clientes_vencido_efetivos, info_clientes_vencido_teste
from data.dao.efetivosDAO import add_efetivos, clientes_vencidos_efetivos, renovar_assinatura_resgatar, renovar_assinatura_salvar, buscar_cliente_efetivo_id
from data.dao.testesDAO import buscar_cliente_teste_id, remover_testes, clientes_vencidos_teste
from data.dao.utilDAO import existencia_id_teste, existencia_id_efetivos
from maneger.exceptions.exceptions_routers import IdExistenteError

def converter_teste_para_efetivo(id):
    situacao = existencia_id_teste(id)
    if situacao:
        clienteTeste = buscar_cliente_teste_id(id)
        novoCliente = TestesTransferencia(clienteTeste[0][1], clienteTeste[0][2])
        add_efetivos(novoCliente.nome, novoCliente.celular, novoCliente.cadastro, novoCliente.vencimento)
        remover_testes(id)
        return f"O cliente '{novoCliente.nome}' foi transferido com sucesso para os efetivos."
    raise IdExistenteError(f"Erro. O ID '{id}' não pertence a nenhum cliente.")

#####################################################################################

def clientes_vencidos_efeti():
    return info_clientes_vencido_efetivos(clientes_vencidos_efetivos())

def clientes_vencidos_tes():
    return info_clientes_vencido_teste(clientes_vencidos_teste())
    
#####################################################################################

def renovar_assinatura(id):
    situacao = existencia_id_efetivos(id)
    if situacao:
        data_str = renovar_assinatura_resgatar(id)
        data = datetime.strptime(data_str, '%Y-%m-%d')
        vencimento = (data + relativedelta(months=1))
        vencimento_str = datetime.strftime(vencimento, '%Y-%m-%d')
        renovar_assinatura_salvar(vencimento_str, id)
        dados = buscar_cliente_efetivo_id(id)
        return f"A mensalidade do cliente '{dados[0][1]}' foi renovada com sucesso!"
    else:
        raise IdExistenteError(f"Erro. O ID '{id}' não pertence a nenhum cliente.")