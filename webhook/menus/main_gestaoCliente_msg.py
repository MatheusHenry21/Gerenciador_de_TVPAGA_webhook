
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

def submenu2_add(phone: str):
    envia_msg(
        phone,
        """ADICIONAR CLIENTES
1 - Adicionar efetivos
2 - Adicionar testes
3 - Voltar

Digite o índice da opção."""
    )

def submenu2_listar(phone: str):
    envia_msg(
        phone,
        """LISTAR CLIENTE
1 - Listar cliente efetivo
2 - Listar cliente teste
3 - Voltar

Digite o índice da opção."""
    )

def submenu2_buscar(phone: str):
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

def submenu2_atualizar(phone: str):
    envia_msg(
        phone,
        """ATUALIZAR CLIENTE
1 - Atualizar cliente efetivo
2 - Atualizar cliente testes
3 - Voltar

Digite o índice da opção."""
    )

def submenu2_remover(phone: str):
    envia_msg(
        phone,
        """REMOVER CLIENTE
1 - Remover cliente efetivo
2 - Remover cliente teste
3 - Voltar

Digite o índice da opção."""
    )