
from webhook.services.whatsapp_client import envia_msg
from handlers.data.DAO import (
    select_etapa,
    resetar_etapas_handler
)
from handlers.data.DAO import (
    update_name,
    update_phone,
    update_id
)

def sub_handler2_nome(phone, text):
    etapa = select_etapa(phone)
    etapaAtual = etapa[4]
    if etapaAtual is None:
        envia_msg(
            phone,
            '''Digite o nome da pessoa
        ''')
        return
    update_name(phone, text)
    return

def sub_handler2_celular(phone, text):
    etapa = select_etapa(phone)
    etapaAtual = etapa[5]
    if etapaAtual is None:
        envia_msg(
            phone,
            '''Digite o celular da pessoa
        ''')
        return
    update_phone(phone, text)
    return

def sub_handler2_id(phone, text):
    etapa = select_etapa(phone)
    etapaAtual = etapa[6]
    if etapaAtual is None:
        envia_msg(
            phone,
            '''Digite o ID da pessoa
        ''')
        return

    update_id(phone, text)
    return

def voltar_menu(phone):
    resetar_etapas_handler(phone)
    envia_msg(
        phone,'''
        Voltando ao menu principal.
    ''')