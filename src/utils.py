import urllib.parse

def clean_search_query(keywords, exclude_terms):
    """Prepara la query para LinkedIn con exclusiones."""
    full_query = f"({keywords}) {exclude_terms}"
    return urllib.parse.quote(full_query)

def generate_linkedin_url(query_formatted, location="Argentina"):
    """
    LinkedIn: f_TPR=r604800 (últimos 7 días).
    f_WT=2%2C3 (Remoto e Híbrido).
    """
    base_url = "https://www.linkedin.com/jobs/search/?"
    return f"{base_url}keywords={query_formatted}&location={location}&f_TPR=r604800&f_WT=2%2C3"

def get_platform_links(role):
    """Genera links para Bumeran y CompuTrabajo con filtros de tiempo y modalidad."""
    q_others = role.lower().replace(" ", "-")
    
    # Bumeran: Esta semana + Híbrido/Remoto
    link_bm = f"https://www.bumeran.com.ar/empleos-busqueda-{q_others}.html?publicado=esta-semana&modalidad=remoto-hibrido"
    
    # CompuTrabajo: Últimos 7 días + Teletrabajo
    link_ct = f"https://ar.computrabajo.com/trabajo-de-{q_others}?pubdate=7&teletrabajo=1"
    
    return link_bm, link_ct