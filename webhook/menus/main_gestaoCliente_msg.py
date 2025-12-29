
from webhook.services.whatsapp_client import envia_msg

def submenu_gestao_cliente(phone: str):
    envia_msg(
        phone,
        """GESTÃO CLIENTES
1 - Adicionar cliente
2 - Listar clientes
3 - Buscar clientes
4 - Atualizar clientes
5 - Remover clientes
6 - Voltar

Digite o índice da opção."""
    )

def submenu_add(phone: str):
    envia_msg(
        phone,
        """ADICIONAR CLIENTES
1 - Adicionar efetivos
2 - Adicionar testes
3 - Voltar

Digite o índice da opção."""
    )

def submenu_buscar(phone: str):
    envia_msg(
        phone,
        """ADICIONAR CLIENTES
1 - Buscar cliente efetivo por nome
2 - Buscar cliente teste por nome
3 - Buscar cliente por celular
4 - Buscar cliente efetivo por id
5 - Buscar cliente teste por id
6 - Voltar

Digite o índice da opção."""
    )

def submenu_atualizar(phone: str):
    envia_msg(
        phone,
        """ATUALIZAR CLIENTE
1 - Atualizar cliente efetivo
2 - Atualizar cliente testes
3 - Voltar

Digite o índice da opção."""
    )

def submenu_remover(phone: str):
    envia_msg(
        phone,
        """ATUALIZAR CLIENTE
1 - Remove cliente efetivo
2 - Remove cliente testes
3 - Voltar

Digite o índice da opção."""
    )