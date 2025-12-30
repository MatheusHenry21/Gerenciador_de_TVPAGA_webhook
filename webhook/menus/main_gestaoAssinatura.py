
from webhook.services.whatsapp_client import envia_msg

def submenu_assinatura(phone):
    envia_msg(
        phone,
        """GESTÂO ASSINATURA
1 - Listar cliente vencidos
2 - Renovar assinatura
3 - Converter teste -> efetivo

Digite o índice da opção."""
    )

def submenu2_assinatura(phone):
    envia_msg(
        phone,
        """CLIENTES VENCIDOS
1 - Clientes efetivos
2 - Clientes testes
3 - Voltar

Digite o índice da opção."""
    )