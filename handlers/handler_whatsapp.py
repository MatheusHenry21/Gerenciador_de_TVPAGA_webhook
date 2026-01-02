
from handlers.gestaoClientes.handlerGestaoClientes import handler_gestao_gestao as gestao_cliente
from handlers.gestaoAssinatura.handlerGestaoAssinatura import handler_gestao_assinatura as gestao_assinatura
from handlers.relatorio.handlerRelatorio import handler_relatorio as relatorio
from handlers.configuracoes.handlerConfiguracoes import handler_configuracoes as configuracoes
from handlers.data.DAO import select_etapa, update_main
from webhook.menus.main_principal import menu_principal

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
            menu_principal(celular)
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