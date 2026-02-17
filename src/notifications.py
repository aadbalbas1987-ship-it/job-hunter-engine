import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_telegram(message):
    try:
        token = os.getenv("TELEGRAM_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Error en Telegram: {e}")

def send_email(subject, body_html):
    try:
        remitente = os.getenv("SMTP_EMAIL")
        password = os.getenv("SMTP_PASSWORD")
        destino = os.getenv("PERSONAL_EMAIL")
        
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destino
        msg['Subject'] = subject
        msg.attach(MIMEText(body_html, 'html'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(remitente, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Error en Email: {e}")