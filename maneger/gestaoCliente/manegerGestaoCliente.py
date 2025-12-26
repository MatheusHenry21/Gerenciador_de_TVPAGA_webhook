
from moldels.moldeContato import Efetivos, Testes
from moldels.moldeContato import info_cliente_efetivo, info_cliente_teste
from moldels.formatacao_dados import formatacao_celular
from moldels.atualizarCliente import dados_atualizar
from data.dao.testesDAO import add_testes, remover_testes, buscar_cliente_teste_id, listar_testes, buscar_cliente_teste_celular, buscar_cliente_teste_nome, atualizar_nome_cliente_teste, atualizar_celular_cliente_teste
from data.dao.efetivosDAO import add_efetivos, remover_efetivos, buscar_cliente_efetivo_id, listar_efetivos, buscar_cliente_efetivo_celular, buscar_cliente_efetivo_nome, atualizar_celular_cliente_efetivo, atualizar_nome_cliente_efetivo
from data.dao.utilDAO import existencia_id_efetivos, existencia_id_teste, existencia_celular_efetivos, existencia_celular_testes, existencia_nome_efetivos, existencia_nome_testes
from maneger.exceptions.exceptions_routers import (
    DadosExistenteError,
    IdExistenteError
    )


def cadastrar_efetivos(nome, celular):
    novoCliente = Efetivos(nome, celular)
    add_efetivos(novoCliente.nome, novoCliente.celular, novoCliente.cadastro, novoCliente.vencimento)
    return {"msg": f"Contato '{novoCliente.nome}'adicionado aos efetivos"}

def cadastrar_testes(nome, celular):         
    novoCliente = Testes(nome, celular)
    add_testes(novoCliente.nome, novoCliente.celular, novoCliente.cadastro, novoCliente.fimTeste)     
    return {"msg": f"Contato '{novoCliente.nome}' adicionado aos testes"}


#####################################################################################

def listar_clientes_efetivos():
    return info_cliente_efetivo(listar_efetivos())

def listar_clientes_testes():
    return info_cliente_teste(listar_testes())

#####################################################################################


def buscar_por_nome_efetivo(nome):
    efetivos = existencia_nome_efetivos(nome)
    if efetivos:
        nome = nome.title()
        return info_cliente_efetivo(buscar_cliente_efetivo_nome(nome))
    raise DadosExistenteError(f"Erro. O nome '{nome}' não pertence a nenhum cliente.")

def buscar_por_nome_teste(nome):
    testes = existencia_nome_testes(nome)
    if testes:
        nome = nome.title()
        return info_cliente_teste(buscar_cliente_teste_nome(nome))
    raise DadosExistenteError(f"Erro. O nome '{nome}' não pertence a nenhum cliente.")


def buscar_celular(celular):
    celular = formatacao_celular(str(celular))

    efetivos = existencia_celular_efetivos(celular)
    testes = existencia_celular_testes(celular)

    if efetivos:
        return info_cliente_efetivo(buscar_cliente_efetivo_celular(celular))
    elif testes:
        return info_cliente_teste(buscar_cliente_teste_celular(celular))
    raise DadosExistenteError(f"Erro. O número '{celular}' não pertence a nenhum cliente.")


def buscar_id_efetivo(id):
    efetivo = existencia_id_efetivos(id)
    if efetivo:
        return info_cliente_efetivo(buscar_cliente_efetivo_id(id))
    raise DadosExistenteError(f"Erro. O ID '{id}' não pertence a nenhum cliente.")

def buscar_id_teste(id):
    teste = existencia_id_teste(id)
    if teste:
        return info_cliente_teste(buscar_cliente_teste_id(id))
    raise DadosExistenteError(f"Erro. O ID '{id}' não pertence a nenhum cliente.")


#####################################################################################


def atualizar_teste(id, nome, celular):
    situacaoT = existencia_id_teste(id)
    if situacaoT:
        novosInfo = dados_atualizar(nome, celular)
        if not novosInfo:
            cliente_dados = buscar_cliente_teste_id(id)
            return f"Nada foi alterado no cliente '{cliente_dados[0][1]}'!"
        if novosInfo[0] is not None:
            atualizar_nome_cliente_teste(novosInfo[0], id)
        if novosInfo[1] is not None:
            atualizar_celular_cliente_teste(novosInfo[1], id)
        cliente_dados = buscar_cliente_teste_id(id)
        return f"O cliente '{cliente_dados[0][1]}' foi alterado com sucesso!"
    else: 
        raise IdExistenteError("Cliente inexistente.")

def atualizar_efetivo(id, nome, celular):
    situacaoE = existencia_id_efetivos(id)
    if situacaoE:
        novosInfo = dados_atualizar(nome, celular)
        if not novosInfo:
            cliente_dados = buscar_cliente_efetivo_id(id)
            return f"Nada foi alterado no cliente '{cliente_dados[0][1]}'!"
        if novosInfo[0] is not None:
            atualizar_nome_cliente_efetivo(novosInfo[0], id)
        if novosInfo[1] is not None:
            atualizar_celular_cliente_efetivo(novosInfo[1], id)

        cliente_dados = buscar_cliente_efetivo_id(id)
        return f"O cliente '{cliente_dados[0][1]}' foi alterado com sucesso!"
    else:
        raise IdExistenteError("Cliente inexistente.")

#####################################################################################

def deletar_efetivo(id):
    situacaoE = existencia_id_efetivos(id)
    if situacaoE:
        remover_efetivos(id)
        return "Cliente excluído!"
    raise IdExistenteError("id não encontrado!")

def deletar_teste(id):
    situacaoT = existencia_id_teste(id)
    if situacaoT:
        remover_testes(id)
        return "Cliente excluído!"
    raise IdExistenteError("id não encontrado!")