
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

def main_gestao_gestao(phone, text):
    pass

def cadastrar_cliente_efetivos(nome, celular):
    try:
        return {"msg": cadastrar_efetivos(
            nome,
            celular
            )}
    except NumeroExistenteError:
        pass
    except NomeVazio:
        pass

def cadastrar_cliente_teste(nome, celular):
    try:
        return {"msg": cadastrar_testes(
            nome,
            celular
            )}
    except NumeroExistenteError:
        pass
    except NomeVazio:
        pass

#####################################################################################

@router.put("/atualizar_efetivo")
def atualizar_cliente_efetivo(id, nome, celular):
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
    