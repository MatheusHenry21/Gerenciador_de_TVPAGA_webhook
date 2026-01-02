
import os
from fastapi import (
    APIRouter,
    Request,
    Response
    )
from handlers.handler_whatsapp import handler_main

router = APIRouter()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "cor2025")

@router.get("/whatsapp")
async def webhook_token(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return Response(content=challenge, media_type="text/plain")
    return Response(status_code=403)

@router.post("/whatsapp")
async def response_webhook(request: Request):
    try:
        payload = await request.json()
        if "entry" not in payload or not payload["entry"]:
            return {"status": "NO_ENTRIES"}
        entry = payload["entry"][0]
        if "changes" not in entry or not entry["changes"]:
            return {"status": "NO_CHANGES"}
        change = entry["changes"][0]
        if "value" not in change or "messages" not in change["value"] or not change["value"]["messages"]:
            return {"status": "NO_MESSAGES"}
        messages = change["value"]["messages"][0]
        if "text" not in messages or "body" not in messages["text"]:
            return {"status": "NO_TEXT"}
        texto = messages["text"]["body"].strip().lower()
        celular = messages["from"]
        handler_main(celular, texto)
        return {"status": "EVENT_RECEIVED"}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}
