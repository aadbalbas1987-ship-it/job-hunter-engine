import urllib.parse

def clean_search_query(keywords, exclude_terms):
    """
    Formatea las palabras clave para que sean compatibles con una URL de LinkedIn.
    Asegura que los términos excluidos siempre se apliquen.
    """
    # Combinamos las keywords con las exclusiones usando el formato de LinkedIn
    full_query = f"({keywords}) {exclude_terms}"
    return urllib.parse.quote(full_query)

def generate_linkedin_url(query_formatted, location="Argentina"):
    """
    Construye la URL final con filtros de tiempo (últimas 24hs).
    """
    base_url = "https://www.linkedin.com/jobs/search/?"
    # f_TPR=r86400 es el filtro para las últimas 24 horas
    return f"{base_url}keywords={query_formatted}&location={location}&f_TPR=r86400" 
