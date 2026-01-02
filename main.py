
from fastapi import FastAPI

from data.dbCreate.database import(
    tabela_clientes_efetivos,
    tabela_clientes_testes
    )
from handlers.data.table_sequencia import estado_conversa
from webhook.webhook_whatsapp import router as mainPrincipal

app = FastAPI()

@app.on_event("startup")
def criar_banco():
    tabela_clientes_efetivos()
    tabela_clientes_testes()
    estado_conversa()

app.include_router(
    mainPrincipal,
    prefix="/webhook",
    tags=["Webhook - Whatsapp"]
)