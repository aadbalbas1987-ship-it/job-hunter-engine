import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_telegram(message):
    token = os.environ.get("TELEGRAM_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print("❌ Error: Faltan variables de Telegram en el sistema.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"❌ Falló envío de Telegram: {e}")

def send_email(subject, body_html):
    remitente = os.environ.get("SMTP_EMAIL")
    password = os.environ.get("SMTP_PASSWORD")
    destino = os.environ.get("PERSONAL_EMAIL")
    
    if not all([remitente, password, destino]):
        print("❌ Error: Faltan variables de Email en el sistema.")
        return

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destino
    msg['Subject'] = subject
    msg.attach(MIMEText(body_html, 'html'))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(remitente, password)
            server.send_message(msg)
    except Exception as e:
        print(f"❌ Falló envío de Email: {e}")