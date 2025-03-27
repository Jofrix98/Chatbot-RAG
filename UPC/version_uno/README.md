# DGSI Web Scraper Project

Este proyecto está diseñado para rastrear páginas web y convertir su contenido HTML a archivos Markdown. Para ello, utiliza Python y las bibliotecas `requests`, `BeautifulSoup4`, y `html2text`. Además, se configura una documentación con `mkdocs` y `mkdocs-material` para facilitar la visualización.

## Instalación

### 1. Crear un nuevo entorno con Conda

Para crear un entorno conda para el proyecto, usa el siguiente comando:

```bash
conda create -n fib_scraper python=3.10 -y
```

### 2. Activar el entorno

Activa el entorno creado con:

```bash
conda activate fib_scraper
```

### 3. Instalar dependencias

Instala las bibliotecas necesarias utilizando pip:

```bash
pip install requests beautifulsoup4 html2text
```

Instala también `mkdocs-material` para la documentación:

```bash
pip install mkdocs-material
```

## Visualización de la Documentación

Para visualizar la documentación de este proyecto, usa el siguiente comando:

```bash
mkdocs serve
```

Este comando iniciará un servidor local que te permitirá acceder a la documentación desde tu navegador en `http://127.0.0.1:8000/`.

## Uso

Este proyecto permite realizar un web scraping en la web de la FIB y almacenar los resultados como archivos Markdown.

1. **Configura la URL base**: `base_url` debe ser la URL del sitio web que deseas rastrear.
2. **Define la carpeta de salida**: `output_folder` es donde se almacenarán los archivos Markdown generados.
3. **Especifica la cantidad máxima de páginas a rastrear**: `max_pages` limita el número de páginas a procesar.

Ejecuta el script con:

```bash
python md.py
```

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
