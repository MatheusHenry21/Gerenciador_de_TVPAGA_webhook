
from data.testeUnique.cadastroCelular import check_unique_celular
from maneger.exceptions.exceptions_routers import (
    NumeroExistenteError,
    NomeVazio
    )

def nome_formatacao(nome):
    if not nome or nome == '' or nome == None:
        raise NomeVazio("Nome não pode está vazio")
    nome = nome.title()
    return nome

def formatacao_celular(celular):
    if len(celular) == 10:
        celular10 = (f"({celular[:2]})9{celular[2:6]}-{celular[6:]}")
        return celular10
    
    elif len(celular) == 11:
        celular11 = (f"({celular[:2]}){celular[2:7]}-{celular[7:]}")
        return celular11

def celular_novo_contato(numCelular):
    celularTeste = formatacao_celular(str(numCelular))
    celular = celularTeste
    teste = check_unique_celular(celularTeste)

    if not teste:
        return celular
    
    raise NumeroExistenteError("Celular já existente.")