
from webhook.services.whatsapp_client import envia_msg
from handlers.data.DAO import(
    select_etapa,
    update_submain2
    )
from maneger.exceptions.exceptions_routers import DadosExistenteError
from maneger.gestaoCliente.manegerGestaoCliente import(
    buscar_por_nome_efetivo,
    buscar_por_nome_teste,
    buscar_celular,
    buscar_id_efetivo,
    buscar_id_teste
)
from webhook.menus.main_gestaoCliente_msg import submenu2_buscar
from webhook.menus.submain_util import(
    sub_handler2_nome,
    sub_handler2_celular,
    sub_handler2_id,
    voltar_menu,
    resetar_etapas_handler
)
from handlers.data.DAO import(
    update_name,
    update_phone,
    update_id
)


def sub_handler_buscar(phone, text):
    SUBMAIN = {
        "1": "NOME_EFETIVO",
        "2": "NOME_TESTE",
        "3": "CELULAR",
        "4": "ID_EFETIVO",
        "5": "ID_TESTE",
        "6": "VOLTAR"
    }
    etapa = select_etapa(phone)
    estadoAtual = etapa[3]

    if estadoAtual is None:
        submenu2_buscar(phone)
        return
    
    novoEstado = SUBMAIN[text]
    update_submain2(phone, text)

    if novoEstado == "NOME_EFETIVO" or novoEstado == "NOME_TESTE":
        nome = etapa[4]
        if nome is None:
            sub_handler2_nome(
                phone,
                text
                )
            return
        
        novoEstado = etapa[4]
        update_name(phone, novoEstado)
        
        if novoEstado == "NOME_EFETIVO":
            try:
                envia_msg(
                    phone,
                    f"Cliente: {buscar_por_nome_efetivo(nome)}"
                )
                resetar_etapas_handler(phone)
            except DadosExistenteError as e:
                envia_msg(
                    phone,
                    e
                )
                resetar_etapas_handler(phone)

        elif novoEstado == "NOME_TESTE":
            try:
                envia_msg(
                    phone,
                    f"Cliente: {buscar_por_nome_teste(nome)}"
                )
                resetar_etapas_handler(phone)
            except DadosExistenteError as e:
                envia_msg(
                    phone,
                    e
                )
                resetar_etapas_handler(phone)
        return

    if novoEstado == "CELULAR":
        celular = etapa[5]
        if celular is None:
            sub_handler2_celular(
                phone,
                text
            )
            return
        
        novoEstado = etapa[4]
        update_phone(phone, celular)

        try:
            envia_msg(
                phone,
                buscar_celular(celular)
            )
        except DadosExistenteError as e:
            envia_msg(
                phone,
                e
            )

    if novoEstado == "ID_EFETIVO" or novoEstado == "ID_TESTE":
        id = etapa[6]

        if id is None:
            sub_handler2_id(phone, text)
            return
        
        novoEstado = etapa[4]
        update_id(phone, id)
        
        if novoEstado == "ID_EFETIVO":
            try:
                envia_msg(
                    phone,
                    f"Cliente: {buscar_id_efetivo(id)}"
                )
                resetar_etapas_handler(phone)

            except DadosExistenteError as e:
                envia_msg(
                    phone,
                    e,
                )
                resetar_etapas_handler(phone)

        elif novoEstado == "ID_TESTE":
            try:
                envia_msg(
                    phone,
                    f"Cliente: {buscar_id_teste(id)}"
                )
                resetar_etapas_handler(phone)

            except DadosExistenteError as e:
                envia_msg(
                    phone,
                    e,
                )
                resetar_etapas_handler(phone)
        return
    
    elif novoEstado == "VOLTAR":
        voltar_menu(phone)
        return