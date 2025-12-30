
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

etapa = select_etapa()

def submain2_nome(phone, text):
    estapaAtual = etapa[4]
    if estapaAtual is None:
        envia_msg(
            phone,
            '''Digite o nome da pessoa
        ''')
        return
    name = update_name(phone, text)
    return name

def submain2_celular(phone, text):
    estapaAtual = etapa[5]
    if estapaAtual is None:
        envia_msg(
            phone,
            '''Digite o celular da pessoa
        ''')
        return
    cllr = update_phone(phone, text)
    return cllr

def submain2_id(phone, text):
    estapaAtual = etapa[6]
    if estapaAtual is None:
        envia_msg(
            phone,
            '''Digite o ID da pessoa
        ''')
        return
    
    id = update_id(phone, text)
    return id

def voltar_menu(phone):
    resetar_etapas_handler(phone)
    envia_msg(
        phone,'''
        Voltando ao menu principal.
    ''')