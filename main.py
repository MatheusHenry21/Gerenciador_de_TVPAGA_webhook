
from fastapi import FastAPI

from data.dbCreate.database import(
    tabela_clientes_efetivos,
    tabela_clientes_testes
    )
from handlers.data.table_sequencia import create_table_sequent
from webhook.webhook_whatsapp import router as mainPrincipal

app = FastAPI()

@app.on_event("startup")
def criar_banco():
    tabela_clientes_efetivos()
    tabela_clientes_testes()
    create_table_sequent()

app.include_router(
    mainPrincipal,
    prefix="/webhook",
    tags=["Webhook - Whatsapp"]
)