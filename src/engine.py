import os
from datetime import datetime
from utils import clean_search_query, generate_linkedin_url
from notifications import send_telegram, send_email

# Configuración de búsqueda
KEYWORDS = ["Python Automation", "Data Analysis", "Process Automation"]
EXCLUDE = "-contable -accounting -auditor -tax"

def run_job_search():
    fecha = datetime.now().strftime('%d/%m/%Y')
    print(f"🚀 Iniciando búsqueda para el día: {fecha}")
    
    report_text = f"🤖 *Job Hunter Report - {fecha}*\n\n"
    html_email = f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <h2 style="color: #2e6c80;">Reporte Diario de Vacantes (Andrés)</h2>
            <p>Se han filtrado resultados de LinkedIn evitando perfiles contables.</p>
            <ul>
    """
    
    for kw in KEYWORDS:
        query_cleaned = clean_search_query(kw, EXCLUDE)
        url = generate_linkedin_url(query_cleaned)
        
        # Formateo para Telegram
        report_text += f"📍 *{kw}*\n[Ver vacantes en LinkedIn]({url})\n\n"
        # Formateo para Email
        html_email += f"<li><strong>{kw}:</strong> <a href='{url}'>Ver vacantes</a></li>"

    html_email += "</ul><br><p>Sistema ejecutado desde el entorno seguro de Windows.</p></body></html>"

    # Ejecución de envíos
    print("Enviando reporte a Telegram...")
    send_telegram(report_text)
    
    print("Enviando reporte a Email...")
    send_email(f"Reporte de Vacantes Automation - {fecha}", html_email)
    
    print("✅ ¡Proceso finalizado con éxito!")

if __name__ == "__main__":
    run_job_search()