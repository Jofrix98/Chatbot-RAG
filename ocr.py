import requests
from pdf2image import convert_from_path
import pytesseract
from io import BytesIO
import os

# Función para descargar el PDF desde una URL
def download_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"Error al descargar el PDF, estado: {response.status_code}")

# Función para convertir el PDF a imágenes
def pdf_to_images(pdf_data):
    # Guardamos el PDF en una ruta temporal
    with open('/content/temp.pdf', 'wb') as f:
        f.write(pdf_data.read())

    # Convertimos el PDF a imágenes
    images = convert_from_path('/content/temp.pdf', 300)  # 300 es la resolución de la imagen
    return images

# Función para aplicar OCR y extraer texto
def ocr_from_images(images):
    extracted_text = ''
    for page in images:
        text = pytesseract.image_to_string(page)
        extracted_text += text + '\n'
    return extracted_text

# Función principal para obtener el texto desde una lista de URLs de PDF
def pdf_to_txt(urls, output_dir):
    # Aseguramos que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)

    for i, url in enumerate(urls):
        # Descargar el PDF
        try:
            pdf_data = download_pdf(url)

            # Convertir el PDF a imágenes
            images = pdf_to_images(pdf_data)

            # Extraer el texto con OCR
            text = ocr_from_images(images)

            # Definir el nombre del archivo de salida
            output_txt_file = os.path.join(output_dir, f'output_{i + 1}.txt')

            # Guardar el texto en un archivo .txt
            with open(output_txt_file, 'w', encoding='utf-8') as f:
                f.write(text)

            print(f'Texto guardado en: {output_txt_file}')

        except Exception as e:
            print(f"Error procesando el PDF de {url}: {e}")

# Ejemplo de uso
pdf_urls = [
    'https://arxiv.org/pdf/2302.01048',  # Reemplaza con tus URLs de PDF
    'https://arxiv.org/pdf/2302.01049'   # Otra URL de ejemplo
]

output_directory = '/content/output_pdfs'  # Directorio donde se guardarán los archivos de texto
pdf_to_txt(pdf_urls, output_directory)
