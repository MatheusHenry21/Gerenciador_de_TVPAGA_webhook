
from handlers.gestaoClientes.subHandlerBuscarCliente import sub_handler_buscar
from webhook.services.whatsapp_client import envia_msg
from maneger.gestaoCliente.manegerGestaoCliente import(
    cadastrar_efetivos,
    cadastrar_testes,
    atualizar_efetivo,
    atualizar_teste,
    deletar_efetivo,
    deletar_teste
)
from handlers.data.DAO import (
    select_etapa,
    update_submain,
    update_submain2
    )
from webhook.menus.main_gestaoCliente_msg import (
    submenu_gestao_cliente,
    submenu2_add,
    submenu2_listar,
    submenu2_atualizar,
    submenu2_remover
    )
from maneger.gestaoCliente.manegerGestaoCliente import(
    listar_clientes_efetivos,
    listar_clientes_testes
)
from webhook.menus.submain_util import (
    voltar_menu,
    resetar_etapas_handler,
    sub_handler2_nome,
    sub_handler2_celular,
    sub_handler2_id
    )
from maneger.exceptions.exceptions_routers import (
    NumeroExistenteError,
    IdExistenteError,
    )

def handler_gestao_gestao(phone, text):
    SUBMAIN = {
        "1": "ADICIONAR",
        "2": "LISTAR",
        "3": "BUSCAR",
        "4": "ATUALIZAR",
        "5": "REMOVER",
        "6": "VOLTAR"
    }
    
    etapa = select_etapa(phone)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if text not in SUBMAIN:
            submenu_gestao_cliente(phone)
            return
        
        estadoNovo = SUBMAIN[text]
        update_submain(phone, estadoNovo)

        if estadoNovo == "ADICIONAR":
            sub_handler2_add(phone, text) #
        elif estadoNovo == "LISTAR":
            sub_handler2_read(phone, text) #
        elif estadoNovo == "BUSCAR":
            sub_handler_buscar(phone, text) #
        elif estadoNovo == "ATUALIZAR":
            sub_handler2_update(phone, text)
        elif estadoNovo == "REMOVER":
            sub_handler2_delete(phone, text) #
        elif estadoNovo == "VOLTAR":
            voltar_menu(phone)
        return

def sub_handler2_add(phone, text):
    SUBMAIN2 = {
        "1": "EFETIVO",
        "2": "TESTE",
        "3": "VOLTAR"
    }

    etapa = select_etapa(etapa)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if text not in SUBMAIN2:
            submenu2_add(phone)
            return
        
        estadoNovo = SUBMAIN2[text]
        update_submain2(phone, estadoNovo)

        nome = etapa[4]
        if nome is None:
            sub_handler2_celular(phone, text)
            return
        celular = etapa[5]
        if celular is None:
            sub_handler2_celular(phone, text)
            return

        if estadoNovo == "EFETIVO":
            try: 
                envia_msg(
                    phone,
                    cadastrar_efetivos(nome, celular)
                )
            except NumeroExistenteError:
                pass
            
        elif estadoNovo == "TESTE":
            try:
                envia_msg(
                    phone,
                    cadastrar_testes(nome, celular)
                )
            except NumeroExistenteError:
                pass

        elif estadoNovo == "VOLTAR":
            voltar_menu(phone)
        return

def sub_handler2_read(phone, text):
    SUBMAIN2 = {
        "1": "EFETIVO",
        "2": "TESTE",
        "3": "VOLTAR"
    }

    etapa = select_etapa(phone, text)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if text not in SUBMAIN2:
            submenu2_listar(phone)
            return
        
        estadoNovo = SUBMAIN2[text]
        update_submain2(phone, estadoNovo)

        if estadoNovo == "EFETIVO":
            envia_msg(
                phone,
                f"Clientes efetivos: {listar_clientes_efetivos()}"
            )
            resetar_etapas_handler(phone)
        elif estadoNovo == "TESTE":
            envia_msg(
                phone,
                f"Clientes testes: {listar_clientes_testes()}"
            )
            resetar_etapas_handler(phone)

        elif estadoNovo == "VOLTAR":
            voltar_menu(phone)
        return

def sub_handler2_update(phone, text):
    SUBMAIN2 = {
        "1": "EFETIVO",
        "2": "TESTE",
        "3": "VOLTAR"
    }

    etapa = select_etapa(phone)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if text not in SUBMAIN2:
            submenu2_atualizar(phone)
            return
        
        estadoNovo = SUBMAIN2[text]
        update_submain2(phone, estadoNovo)

        if estadoNovo == "EFETIVO":
            pass
        elif estadoNovo == "TESTE":
            pass
        elif estadoNovo == "VOLTAR":
            voltar_menu(phone)
        return

def sub_handler2_delete(phone, text):
    SUBMAIN2 = {
    "1": "EFETIVO",
    "2": "TESTE",
    "3": "VOLTAR"
}

    etapa = select_etapa(phone)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if text not in SUBMAIN2:
            submenu2_remover(phone)
            return
        
        estadoNovo = SUBMAIN2[text]
        update_submain2(phone, estadoNovo)

        id = etapa[6]
        if id is None:
            submain2_id(phone, text)
            return
        
        if estadoNovo == "EFETIVO":
            try:
                envia_msg(
                    phone,
                    deletar_efetivo(id)
                )
            except IdExistenteError:
                pass
            
        elif estadoNovo == "TESTE":
            try:
                envia_msg(
                    phone,
                    deletar_teste(id)
                    )
            except IdExistenteError:
                pass

        elif estadoNovo == "VOLTAR":
            voltar_menu(phone)
        return

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