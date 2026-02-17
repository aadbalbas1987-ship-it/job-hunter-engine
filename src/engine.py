import os
from dotenv import load_dotenv
from notifications import send_telegram, send_email
from utils import clean_search_query, generate_linkedin_url

load_dotenv()

# Filtro estricto: Cero contabilidad
KEYWORDS = ["Python Automation", "Data Analysis", "Process Automation"]
EXCLUDE = "-contable -accounting -auditor -tax"

def run_job_search():
    print("🚀 Iniciando búsqueda de empleos...")
    report_text = "*Nuevas Vacantes de Automation & Data (24h)*\n\n"
    html_email = "<h2>Reporte Diario de Vacantes</h2><ul>"
    
    for kw in KEYWORDS:
        # Usamos las funciones de utils.py
        query_cleaned = clean_search_query(kw, EXCLUDE)
        url = generate_linkedin_url(query_cleaned)
        
        report_text += f"📍 *{kw}*\n[Ver vacantes en LinkedIn]({url})\n\n"
        html_email += f"<li><strong>{kw}:</strong> <a href='{url}'>Ver en LinkedIn</a></li>"

    html_email += "</ul><p>Filtros aplicados: Sin referencias contables.</p>"

    # Envíos
    print("Enviando Telegram...")
    send_telegram(report_text)
    
    print("Enviando Email...")
    send_email("Tu Reporte Diario de Empleos Python", html_email)
    
    print("✅ ¡Proceso completado! Revisa tu celular y tu casilla de correo.")

if __name__ == "__main__":
    run_job_search()