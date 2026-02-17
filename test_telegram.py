import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

print(f"Probando con Token: {token[:5]}... e ID: {chat_id}")

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = {"chat_id": chat_id, "text": "HOLA ANDRÉS! Si lees esto, el bot funciona."}

try:
    r = requests.post(url, json=data)
    print(f"Respuesta de Telegram: {r.status_code}")
    print(r.json())
except Exception as e:
    print(f"Error fatal: {e}")