
from webhook.services.whatsapp_client import envia_msg
from maneger.configuracoes.manegerConfiguracoes import resetar_banco
from webhook.menus.main_configuracao_msg import (
    submain_configuracoes,
    submain_configuracoes_confirmacao
    )
from handlers.data.DAO import (
    select_etapa,
    update_submain,
    update_submain2,
    resetar_etapas_handler
    )
from webhook.menus.submain_util import voltar_menu

def handler_configuracoes(celular, texto):
    SUBMAIN = {
        "1": "RESETAR_DADOS",
        "2": "VOLTAR"
    }

    etapa = select_etapa(celular)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if texto not in SUBMAIN:
            submain_configuracoes(celular)
            return
    
        novoEstado = SUBMAIN[texto]
        update_submain(celular, novoEstado)

        if novoEstado == "RESETAR_DADOS":
            sub_handler_confirmacao(celular, texto)
        elif novoEstado == "VOLTAR":
            voltar_menu(celular)
        return

def sub_handler_confirmacao(celular, texto):
    SUBMAIN2 = {
        "1": "SIM",
        "2": "NAO"
    }

    etapa = select_etapa(celular)
    estado_atual = etapa[3]

    if estado_atual is None:
        if texto not in SUBMAIN2:
            submain_configuracoes_confirmacao(celular)
            return
        
        estadoNovo = SUBMAIN2[texto]
        update_submain2(celular, estadoNovo)

        if estadoNovo == "SIM":
            situacao = resetar_banco()
            envia_msg(
                celular,
                situacao
                )
            resetar_etapas_handler(celular)
        elif estadoNovo == "NAO":
            voltar_menu(celular)
        return