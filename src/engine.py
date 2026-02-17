import os
import csv
from datetime import datetime
from utils import clean_search_query, generate_linkedin_url, get_platform_links
from notifications import send_telegram, send_email

# Configuración de Roles
ROLES = [
    "Data Analyst", 
    "Analista de Datos", 
    "Administrativo Semi Senior", 
    "Administrativo Senior",
    "Analista de Procesos",
    "Business Intelligence"
]

EXCLUDE = "-contable -accounting -auditor -tax -impuestos -facturacion"
DATA_FILE = "data/historico_vacantes.csv"

def save_to_csv(role, platform, url):
    """Guarda la vacante en el CSV para análisis posterior."""
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.isfile(DATA_FILE)
    fecha = datetime.now().strftime('%Y-%m-%d')
    
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Fecha', 'Puesto', 'Plataforma', 'Link'])
        writer.writerow([fecha, role, platform, url])

def run_job_search():
    fecha_display = datetime.now().strftime('%d/%m/%Y')
    print(f"🚀 Iniciando búsqueda semanal: {fecha_display}")
    
    report_text = f"🏠 *RADAR SEMANAL: REMOTO/HÍBRIDO - {fecha_display}*\n\n"
    
    for role in ROLES:
        q_linked = clean_search_query(role, EXCLUDE)
        link_ln = generate_linkedin_url(q_linked)
        link_bm, link_ct = get_platform_links(role)

        # Guardamos en nuestra base de datos
        save_to_csv(role, "LinkedIn", link_ln)
        save_to_csv(role, "Bumeran", link_bm)
        save_to_csv(role, "CompuTrabajo", link_ct)

        report_text += f"📍 *{role}*\n"
        report_text += f"• [LinkedIn]({link_ln}) | [Bumeran]({link_bm})\n\n"

    # Enviar notificaciones
    send_telegram(report_text)
    # Reutilizamos el texto de telegram para el email (limpiando markdown simple)
    send_email(f"Reporte Semanal de Vacantes - {fecha_display}", report_text.replace("*", ""))
    print("✅ Proceso completado con éxito.")

if __name__ == "__main__":
    run_job_search()