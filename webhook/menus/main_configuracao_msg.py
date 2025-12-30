
from webhook.services.whatsapp_client import envia_msg

def submain_configuracoes(phone: str):
    envia_msg(
        phone,
        """CONFIGURAÇÕES

1 - Resetar sistema
2 - Voltar

Digite o índice da opção."""
    )

def submain_configuracoes_confirmacao(phone):
    envia_msg(
        phone,
        """⚠️ ATENÇÃO ⚠️
Você tem certeza que deseja RESETAR o sistema?

1 - SIM
2 - NÃO

Digite o índice da opção."""
    )