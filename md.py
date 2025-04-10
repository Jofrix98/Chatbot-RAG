import os
import requests
from bs4 import BeautifulSoup
import html2text
from urllib.parse import urljoin, urlparse, urldefrag
from collections import deque
from pdf2image import convert_from_path
import pytesseract
from io import BytesIO

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
    """Extrae enlaces internos HTML y PDF de la web."""
    soup = BeautifulSoup(html, 'html.parser')
    html_links = set()
    pdf_links = set()

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        full_url = urljoin(base_url, href)
        full_url, _ = urldefrag(full_url)
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            if full_url.lower().endswith('.pdf'):
                pdf_links.add(full_url)
            else:
                html_links.add(full_url)

    return html_links, pdf_links

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

def FUNCTION(pdf_url, output_folder):
    """Procesa el PDF con OCR y guarda el texto extraído."""
    try:
        print(f"Procesando PDF con OCR: {pdf_url}")
        response = requests.get(pdf_url)
        if response.status_code != 200:
            raise Exception(f"Error al descargar el PDF, estado: {response.status_code}")
        
        # Guardar temporalmente el PDF
        temp_pdf_path = os.path.join(output_folder, 'temp.pdf')
        with open(temp_pdf_path, 'wb') as f:
            f.write(response.content)

        # Convertir a imágenes
        images = convert_from_path(temp_pdf_path, 300)

        # Extraer texto con OCR
        extracted_text = ''
        for page in images:
            text = pytesseract.image_to_string(page)
            extracted_text += text + '\n'

        # Nombre de archivo basado en la URL
        filename = urlparse(pdf_url).path.strip('/').replace('/', '_')
        txt_filename = os.path.join(output_folder, f'{filename}.txt')

        # Guardar texto
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write(extracted_text)

        print(f"Texto extraído guardado en: {txt_filename}")
        
        # Limpiar temporal
        os.remove(temp_pdf_path)

    except Exception as e:
        print(f"Error procesando el PDF {pdf_url}: {e}")

def scrape_fib_website(base_url, output_folder, max_pages=10):
    """Rastrea la web de la FIB y guarda el contenido en Markdown y texto OCR de PDFs."""
    visited = set()
    to_visit = deque([(base_url, 0)])

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
            html_links, pdf_links = extract_links(html, base_url)

            for pdf_link in pdf_links:
                FUNCTION(pdf_link, output_folder)

            for link in html_links:
                if link not in visited:
                    to_visit.append((link, depth + 1))

# Configuración
base_url = "https://www.fib.upc.edu/es"
output_folder = "docs"
scrape_fib_website(base_url, output_folder, max_pages=500)
