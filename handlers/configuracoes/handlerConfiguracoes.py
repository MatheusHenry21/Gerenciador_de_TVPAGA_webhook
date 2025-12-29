
from maneger.configuracoes.manegerConfiguracoes import resetar_banco
from webhook.services.whatsapp_client import envia_msg

def main_configuracoes(celular, texto):
    SUBMAIN = {
        "1": "RESETAR_DADOS"
    }

    if texto not in SUBMAIN:
        envia_msg(celular,'''
            CONFIGURAÇÕES

1 - Resetar sistema

Digite o índice da opção.'''
        )
        return
    else:
        resetar_banco()
        return {"msg": "Banco resetado com sucesso"}
