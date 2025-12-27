
from fastapi import FastAPI

from data.dbCreate.database import(
    tabela_clientes_efetivos,
    tabela_clientes_testes
    )
from routers.webhook.webhook_whatsap import router as mainPrincipal

app = FastAPI()

@app.on_event("startup")
def criar_banco():
    tabela_clientes_efetivos()
    tabela_clientes_testes()

app.include_router(
    mainPrincipal,
    prefix="/webhook",
    tags=["Webhook - Whatsapp"]
)