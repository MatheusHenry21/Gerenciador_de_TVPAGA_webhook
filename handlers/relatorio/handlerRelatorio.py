from webhook.menus.main_relatorio import submenu_relatorio
from webhook.menus.submain_util import voltar_menu
from maneger.gestaoCliente.manegerGestaoCliente import listar_clientes_efetivos, listar_clientes_testes
from webhook.services.whatsapp_client import envia_msg
from handlers.data.DAO import select_etapa, update_submain, resetar_etapas_handler

def handler_relatorio(phone, text):
    SUBMAIN = {
        "1": "LISTAR_EFETIVOS",
        "2": "LISTAR_TESTES",
        "3": "VOLTAR"
    }

    etapa = select_etapa(phone)
    estadoAtual = etapa[1]

    if estadoAtual is None:
        if text not in SUBMAIN:
            submenu_relatorio(phone)
            return

        novoEstado = SUBMAIN[text]
        update_submain(phone, novoEstado)

        if novoEstado == "LISTAR_EFETIVOS":
            envia_msg(phone, listar_clientes_efetivos())
            resetar_etapas_handler(phone)
        elif novoEstado == "LISTAR_TESTES":
            envia_msg(phone, listar_clientes_testes())
            resetar_etapas_handler(phone)
        elif novoEstado == "VOLTAR":
            voltar_menu(phone)
        return
