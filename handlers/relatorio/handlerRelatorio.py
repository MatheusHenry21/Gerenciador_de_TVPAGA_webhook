
from webhook.services.whatsapp_client import envia_msg
from webhook.menus.main_relatorio import submenu_relatorio
from moldels.moldeContato import info_clientes_vencendo
from maneger.relatorio.manegerRelatorio import (
    quantidade_efetivos,
    quantidade_testes,
    quantidade_total,
    tempo_para_cobrança
    )
from webhook.menus.submain_util import voltar_menu
from handlers.data.DAO import (
    select_etapa,
    update_submain,
    resetar_etapas_handler
    )


def handler_relatorio(phone, text):
    SUBMAIN = {
        "1": "TOTAL_CLIENTE",
        "2": "TOTAL_EFETIVOS",
        "3": "TOTAL_TESTES",
        "4": "CLIENTE_A_VENCER",
        "5": "VOLTAR"
    }

    etapa = select_etapa(phone)
    estadoAtual = etapa[2]

    if estadoAtual is None:
        if text not in SUBMAIN:
            submenu_relatorio(phone)
            return

        novoEstado = SUBMAIN[text]
        update_submain(phone, novoEstado)

        if novoEstado == "TOTAL_CLIENTE":
            envia_msg(
                phone,
                f'''Total de clientes: {quantidade_total()}
            ''')
            resetar_etapas_handler(phone)
        elif novoEstado == "TOTAL_EFETIVOS":
            envia_msg(
                phone,
                f'''Total de clientes efetivos: {quantidade_efetivos()}
            ''')
            resetar_etapas_handler(phone)
        elif novoEstado == "TOTAL_TESTES":
            envia_msg(
                phone,
                f'''Total de clientes testes: {quantidade_testes()}
            ''')
            resetar_etapas_handler(phone)
        elif novoEstado == "CLIENTE_A_VENCER":
            envia_msg(
                phone,
                f'''Clientes a vencer: {info_clientes_vencendo(tempo_para_cobrança())}
            ''')
            resetar_etapas_handler(phone)
        elif novoEstado == "VOLTAR":
            voltar_menu(phone)
        return