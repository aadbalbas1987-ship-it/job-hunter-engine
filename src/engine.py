import os
import csv
from datetime import datetime
from utils import clean_search_query, generate_linkedin_url, get_platform_links
from notifications import send_telegram, send_email

# Configuración
ROLES = ["Data Analyst", "Analista de Datos", "Administrativo Senior", "Analista de Procesos"]
EXCLUDE = "-contable -accounting -auditor -tax -impuestos"
DATA_FILE = "data/historico_vacantes.csv"

def save_to_csv(role, platform, url):
    """Guarda los datos para el futuro Dashboard."""
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
    report_text = f"📊 *DATA ESTRATÉGICA - {fecha_display}*\n\n"
    
    for role in ROLES:
        # Generar links usando utils
        q_linked = clean_search_query(role, EXCLUDE)
        link_ln = f"{generate_linkedin_url(q_linked)}&f_WT=2%2C3"
        link_bm, link_ct = get_platform_links(role)

        # Guardar en base de datos local (CSV)
        save_to_csv(role, "LinkedIn", link_ln)
        save_to_csv(role, "Bumeran", link_bm)
        save_to_csv(role, "CompuTrabajo", link_ct)

        # Formatear reporte para Telegram
        report_text += f"📍 *{role}*\n"
        report_text += f"• [LinkedIn]({link_ln}) | [Bumeran]({link_bm})\n\n"

    send_telegram(report_text)
    print(f"✅ Reporte enviado y datos guardados en {DATA_FILE}")

if __name__ == "__main__":
    run_job_search()