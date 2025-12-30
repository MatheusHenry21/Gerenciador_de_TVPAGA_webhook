
from webhook.services.whatsapp_client import envia_msg

def submenu_relatorio(phone):
    envia_msg(
        phone,
        """RELATÓRIO
1 - Total clientes
2 - Total clientes efetivos
3 - Total clientes testes
4 - Clientes preste a vencer
5 - Voltar

Digite o índice da opção."""
    )