
from fastapi import (
    APIRouter,
    Request,
    Response
    )
from handler_whatsapp import handler_main

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
    handler_main(payload)
    return {"status": "EVENT_RECEIVED"}