
from webhook.services.whatsapp_client import envia_msg

def menu_principal(phone: str):
    envia_msg(
        phone,
        """MENU PRINCIPAL
1 - Gestão de clientes
2 - Gestão de assinaturas
3 - Relatório
4 - Configurações

Digite o índice da opção."""
    )