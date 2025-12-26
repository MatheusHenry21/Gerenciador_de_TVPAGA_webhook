
from routers.gestaoClientes.routersGestaoClientes import router as gestaoClientes
from routers.gestaoAssinatura.routersGestaoAssinatura import router as gestaoAssinaturas
from routers.relatorio.routersRelatorio import router as relatorio
from routers.configuracoes.routersConfiguracoes import router as configuracoes
from data.dbCreate.database import(
    tabela_clientes_efetivos,
    tabela_clientes_testes
    )

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def criar_banco():
    tabela_clientes_efetivos()
    tabela_clientes_testes()

app.include_router(
    gestaoClientes,
    prefix="/webhook",
    tags=["Clientes"]
)

app.include_router(
    gestaoAssinaturas,
    prefix="/webhook",
    tags=["Assinaturas"]
)

app.include_router(
    relatorio,
    prefix="/webhook",
    tags=["Relatorios"]
)

app.include_router(
    configuracoes,
    prefix="/webhook",
    tags=["Configuracoes"]
)