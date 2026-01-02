
import os
import requests

TOKEN = os.getenv("TOKEN", "cor2025")
PHONE_ID = os.getenv("PHONE_ID", "123")

def envia_msg(telefone, texto):

    url = f"https://graph.facebook.com/v18.0/{PHONE_ID}/messages"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": telefone,
        "type": "text",
        "text":{
            "body": texto
        }
    }

    requests.post(url, json=payload, headers=headers)