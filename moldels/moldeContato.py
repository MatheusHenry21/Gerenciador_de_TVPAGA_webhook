
from .formatacao_dados import(
    celular_novo_contato,
    nome_formatacao
    )

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class Molde():

    def __init__(self, nome, celular):
        self.nome = nome_formatacao(nome)
        self.celular = celular_novo_contato(celular)

class Efetivos(Molde):
    
    def __init__(self, nome, celular):
        super().__init__(nome, celular)
        self.cadastro = date.today()
        self.vencimento = self.cadastro + relativedelta(months=1)

    def __str__(self):
        return f"{self.nome} {self.celular} {self.cadastro:%Y-%m-%d} {self.vencimento:%Y-%m-%d}"

class Testes(Molde):
    def __init__(self, nome, celular):
        super().__init__(nome, celular)
        self.cadastro = datetime.now()
        self.fimTeste = self.cadastro + timedelta(hours=2)
        self.cadastro = self.cadastro.strftime("%Y-%m-%d %H:%M")
        self.fimTeste = self.fimTeste.strftime("%Y-%m-%d %H:%M")
    
    def __str__(self):
        return f"{self.nome} {self.celular} {self.cadastro} {self.fimTeste}"

class TestesTransferencia():
    def __init__(self, nome, celular):
        self.nome = nome
        self.celular = celular
        self.cadastro = date.today()
        self.vencimento = self.cadastro + relativedelta(months=1)

    def __str__(self):
        return f"{self.nome} {self.celular} {self.cadastro} {self.vencimento}"
    
#####################################################################################

def info_cliente_efetivo(lista):
    if not lista:
        return []
    
    cliente = []
    for item in lista:
        inscricao_fmt = f"{item[4][8:]}/{item[4][5:7]}/{item[4][:4]}"
        vencimento_fmt = f"{item[5][8:]}/{item[5][5:7]}/{item[5][:4]}"
        cliente.append({
                "id": item[0],
                "nome": item[1],
                "celular": item[2],
                "plano": item[3],
                "data_inscricao": inscricao_fmt,
                "data_vencimento": vencimento_fmt
                })
    return cliente

def info_cliente_teste(lista):
    if not lista:
        return []
    
    cliente = []
    for item in lista:
        inscricao_fmt = f"{item[4][8:10]}/{item[4][5:7]}/{item[4][:4]} {item[4][11:13]}:{item[4][14:]}"
        vencimento_fmt = f"{item[5][8:10]}/{item[5][5:7]}/{item[5][:4]} {item[5][11:13]}:{item[5][14:]}"
        cliente.append({
                "id": item[0],
                "nome": item[1],
                "celular": item[2],
                "plano": item[3],
                "data_inscricao": inscricao_fmt,
                "fim_teste": vencimento_fmt
                })
    return cliente

#####################################################################################

def info_clientes_vencendo(lista):
    if not lista:
        return []

    cliente = []
    for item in lista:
        dias = int(item[3])
        if dias:
            horas = int((item[3]%dias)*24)
        else:
            horas = int(item[3]*24)
        cliente.append({
                "id": item[0],
                "nome": item[1],
                "celular": item[2],
                "dias_para_vencimento": dias,
                "horas_para_vencimento": horas
                })
    return cliente

#####################################################################################

def info_clientes_vencido_efetivos(lista):
    if not lista:
        return []
    clientes = []

    for item in lista:
        clientes.append({
            "id": item[0],
            "nome": item[1],
            "celular": item[2],
            "dias_vencidos": item[3]
            })
    return clientes

def info_clientes_vencido_teste(lista):
    if not lista:
        return []
    clientes = []

    for item in lista:
        clientes.append({
            "id": item[0],
            "nome": item[1],
            "celular": item[2],
            })
    return clientes