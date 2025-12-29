
from fastapi import (
    APIRouter,
    Request,
    Response
    )
from webhook.handler.handler_whatsapp import handler_main

router = APIRouter()

VERIFY_TOKEN = "cor2025"

@router.get("/whatsapp")
async def webhook_token(request: Request):
    params= request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return Response(content=challenge, media_type="text/plain")
    return Response(status_code=403)

@router.post("/whatsapp")
async def response_webhook(request: Request):
    payload = await request.json()

    messages = payload["entry"][0]["changes"][0]["value"]["messages"][0]

    texto = messages["text"]["body"].strip().lower()
    celular = messages["from"]
    handler_main(celular, texto)

    return {"status": "EVENT_RECEIVED"}