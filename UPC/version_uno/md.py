import os
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from collections import deque

def get_page_content(url):
    """Descarga el contenido de una página y lo devuelve como HTML."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error {response.status_code} al acceder a {url}")
        return None

def extract_links(html, base_url):
    """Extrae los enlaces internos de la web para recorrer más páginas."""
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        full_url, _ = urldefrag(full_url)  # Remove URL fragment
        if urlparse(full_url).netloc == urlparse(base_url).netloc:  # Solo enlaces internos
            links.add(full_url)
    return links

def convert_html_to_markdown(html):
    """Convierte HTML a Markdown manteniendo imágenes y tablas."""
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.ignore_tables = False
    return converter.handle(html)

def save_markdown(content, filename, folder):
    """Guarda el contenido en un archivo Markdown."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Guardado: {path}")

def scrape_fib_website(base_url, output_folder, max_pages=10):
    """Rastrea la web de la FIB y guarda el contenido en Markdown."""
    visited = set()
    to_visit = deque([(base_url, 0)])  # Use deque for BFS, storing (url, depth)

    while to_visit and len(visited) < max_pages:
        url, depth = to_visit.popleft()
        if url in visited:
            continue
        print(f"Procesando: {url}")
        html = get_page_content(url)
        if not html:
            continue
        
        markdown_content = convert_html_to_markdown(html)
        filename = urlparse(url).path.strip('/').replace('/', '_') or 'index'
        save_markdown(markdown_content, f"{filename}.md", output_folder)
        
        visited.add(url)
        if depth < max_pages:
            links = extract_links(html, base_url)
            for link in links:
                if link not in visited:
                    to_visit.append((link, depth + 1))

# Configuración de la web de la FIB
base_url = "https://www.fib.upc.edu/es"
output_folder = "docs"
scrape_fib_website(base_url, output_folder, max_pages=500)
