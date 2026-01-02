
from webhook.menus.submain_util import voltar_menu
from webhook.services.whatsapp_client import envia_msg
from webhook.menus.main_gestaoAssinatura import (
    submenu_assinatura,
    submenu2_assinatura,
    )
from webhook.menus.submain_util import submain2_id
from maneger.exceptions.exceptions_routers import IdExistenteError
from maneger.gestaoAssinatura.manegerGestaoAssinatura import(
    converter_teste_para_efetivo,
    clientes_vencidos_efeti,
    clientes_vencidos_tes,
    renovar_assinatura
    )
from handlers.data.DAO import (
    select_etapa,
    resetar_etapas_handler,
    update_submain,
    update_submain2,
    update_id
    )


def handler_gestao_assinatura(phone, text):
    SUBMAIN = {
        "1": "CLIENTE_VENCIDO",
        "2": "RENOVAR ASSINATURA",
        "3": "CONVERTER_CLIENTE",
        "4": "VOLTAR"
    }

    etapa = select_etapa(phone)
    estadoAtual = etapa[1]

    if estadoAtual is None:
        if text not in SUBMAIN:
            submenu_assinatura(phone)
            return

        novoEstado = SUBMAIN[text]
        update_submain(phone, novoEstado)

        if novoEstado == "CLIENTE_VENCIDO":
            sub_holder_vencidos(phone, text)
        elif novoEstado == "RENOVAR ASSINATURA":
            try:
                id = submain2_id(phone, text)
                envia_msg(
                    phone,
                    renovar_assinatura(id)
                )
                resetar_etapas_handler(phone)
            except IdExistenteError:
                pass

            id = update_id(phone, text)
        elif novoEstado == "CONVERTER_CLIENTE":
            try:
                id = submain2_id(phone, text)
                envia_msg(
                    phone,
                    converter_teste_para_efetivo(id)
                )
                resetar_etapas_handler(phone)
            except IdExistenteError:
                pass

        elif novoEstado == "VOLTAR":
            voltar_menu(phone)
        return



def sub_holder_vencidos(phone, text):
    SUBMAIN2 = {
        "1": "CLIENTES_EFETIVOS",
        "2": "CLIENTES_TESTES",
        "3": "VOLTAR"
    }

    estado = select_etapa(phone)
    novoEstado = estado[1]

    if novoEstado is None:
        if text is not SUBMAIN2:
            submenu2_assinatura(phone)
            return
        
        novoEstado = SUBMAIN2[text]
        update_submain2(phone, novoEstado)

        if novoEstado == "CLIENTES_EFETIVOS":
            envia_msg(
                phone,
                f"Clientes vencidos: {clientes_vencidos_efeti()}"
                )
            resetar_etapas_handler(phone)
        
        elif novoEstado == "CLIENTES_TESTES":
            envia_msg(
                phone,
                f"Clientes vencidos: {clientes_vencidos_tes()}"
                )
            resetar_etapas_handler(phone)
        
        elif novoEstado == "VOLTAR":
            voltar_menu(phone)

        return