import os
from datetime import datetime
from utils import clean_search_query, generate_linkedin_url
from notifications import send_telegram, send_email

ROLES = [
    "Data Analyst", 
    "Analista de Datos", 
    "Administrativo Semi Senior", 
    "Administrativo Senior",
    "Analista de Procesos",
    "Business Intelligence" # Lo sumamos como 'puente' excelente
]

EXCLUDE = "-contable -accounting -auditor -tax -impuestos -facturacion"

def run_job_search():
    fecha = datetime.now().strftime('%d/%m/%Y')
    print(f"🚀 Iniciando búsqueda Híbrida/Remota: {fecha}")
    
    report_text = f"🏠 *MODALIDAD: REMOTO / HÍBRIDO - {fecha}*\n"
    report_text += "🎯 *Foco:* Data & Admin Seniority\n\n"
    
    html_email = f"<h2>Reporte Remoto/Híbrido - {fecha}</h2>"

    for role in ROLES:
        q_linked = clean_search_query(role, EXCLUDE)
        q_others = role.lower().replace(" ", "-")
        
        # --- LINKEDIN (f_WT=2 es remoto, f_WT=3 es híbrido) ---
        # f_TPR=r86400 (24h) | f_WT=2%2C3 (Remoto e Híbrido)
        link_ln = f"{generate_linkedin_url(q_linked)}&f_WT=2%2C3"
        
        # --- BUMERAN (modalidad-remoto / modalidad-hibrido) ---
        link_bm = f"https://www.bumeran.com.ar/empleos-busqueda-{q_others}.html?publicado=en-las-ultimas-24-horas&modalidad=remoto-hibrido"
        
        # --- COMPUTRABAJO (teletrabajo=1 es remoto, 2 es presencial) ---
        # Priorizamos el parámetro de teletrabajo
        link_ct = f"https://ar.computrabajo.com/trabajo-de-{q_others}?pubdate=1&teletrabajo=1"

        report_text += f"📍 *{role}*\n"
        report_text += f"• [LinkedIn (Remoto/Híb)]({link_ln})\n"
        report_text += f"• [Bumeran (Remoto/Híb)]({link_bm})\n"
        report_text += f"• [CompuTrabajo (Remoto)]({link_ct})\n\n"
        
        html_email += f"<h3>{role}</h3><ul>"
        html_email += f"<li><a href='{link_ln}'>LinkedIn (Remoto/Híbrido)</a></li>"
        html_email += f"<li><a href='{link_bm}'>Bumeran (Remoto/Híbrido)</a></li>"
        html_email += f"<li><a href='{link_ct}'>CompuTrabajo (Remoto)</a></li></ul>"

    send_telegram(report_text)
    send_email(f"Trabajos Híbridos/Remotos - {fecha}", html_email)
    print("✅ ¡Reporte enviado con filtros de modalidad!")

if __name__ == "__main__":
    run_job_search()