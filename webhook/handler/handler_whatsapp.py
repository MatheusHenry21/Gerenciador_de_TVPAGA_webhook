
from handlers.gestaoClientes.handlerGestaoClientes import main_gestao_gestao as gestao_cliente
from handlers.gestaoAssinatura.handlerGestaoAssinatura import main_gestao_assinatura as gestao_assinatura
from handlers.relatorio.handlerRelatorio import main_relatorio as relatorio
from handlers.configuracoes.handlerConfiguracoes import main_configuracoes as configuracoes
from webhook.handler.data_handler.DAO import select_etapa, update_main
from webhook.services.whatsapp_client import envia_msg

def handler_main(celular: str, texto: str):
    MAIN = {
        "1": "GESTAO_CLIENTE",
        "2": "GESTAO_ASSINATURA",
        "3": "RELATORIO",
        "4": "CONFIGURACOES"
    }

    etapa = select_etapa(celular)
    estado_atual = etapa[1] if etapa else None

    if estado_atual is None:
        if texto not in MAIN:
            envia_msg(
                celular,
                """MENU PRINCIPAL
1 - Gestão de clientes
2 - Gestão de assinaturas
3 - Relatório
4 - Configurações

Digite o índice da opção."""
            )
            return

        novo_estado = MAIN[texto]
        update_main(celular, novo_estado)

        if novo_estado == "GESTAO_CLIENTE":
            gestao_cliente(celular, texto)
        elif novo_estado == "GESTAO_ASSINATURA":
            gestao_assinatura(celular, texto)
        elif novo_estado == "RELATORIO":
            relatorio(celular, texto)
        elif novo_estado == "CONFIGURACOES":
            configuracoes(celular, texto)

        return
