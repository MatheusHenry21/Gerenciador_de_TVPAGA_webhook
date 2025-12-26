
from moldels.formatacao_dados import celular_novo_contato

def dados_atualizar(nome, celular):
    novo_nome = None
    novo_celular = None

    if nome is not None:
        novo_nome = nome.title()

    if celular is not None:
        novo_celular = celular_novo_contato(celular)

    if novo_nome is None and novo_celular is None:
        return None

    nome = nome.title()
    return [novo_nome, novo_celular]