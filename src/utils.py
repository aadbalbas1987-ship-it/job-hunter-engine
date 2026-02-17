import urllib.parse

def clean_search_query(keywords, exclude_terms):
    """Limpia y prepara la query para LinkedIn."""
    full_query = f"({keywords}) {exclude_terms}"
    return urllib.parse.quote(full_query)

def generate_linkedin_url(query_formatted, location="Argentina"):
    """URL para LinkedIn con filtro de 24hs."""
    base_url = "https://www.linkedin.com/jobs/search/?"
    return f"{base_url}keywords={query_formatted}&location={location}&f_TPR=r86400"

def get_platform_links(role):
    """Genera los links específicos para Bumeran y CompuTrabajo."""
    q_others = role.lower().replace(" ", "-")
    
    # Bumeran: Filtro 24hs + Híbrido/Remoto
    link_bm = f"https://www.bumeran.com.ar/empleos-busqueda-{q_others}.html?publicado=en-las-ultimas-24-horas&modalidad=remoto-hibrido"
    
    # CompuTrabajo: Filtro 24hs + Remoto
    link_ct = f"https://ar.computrabajo.com/trabajo-de-{q_others}?pubdate=1&teletrabajo=1"
    
    return link_bm, link_ct