import chromadb
from sentence_transformers import SentenceTransformer
import markdown
from bs4 import BeautifulSoup

# Cargar modelo de embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Cliente ChromaDB
chroma_client = chromadb.PersistentClient(path="./chromadb_data")  # Cambia a un path local
collection_name = "fib_web_data"
collection = chroma_client.get_or_create_collection(name=collection_name)

# Funciones
def compute_embedding(text):
    """Genera embeddings para el texto usando Sentence Transformers."""
    return embedding_model.encode(text).tolist()

def md_to_text(md_content):
    """Convierte Markdown a texto plano sin etiquetas HTML."""
    html = markdown.markdown(md_content)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def chunk_text(text, chunk_size=200, overlap=25):
    """Divide el texto en fragmentos con solapamiento."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def initialize_collection():
    """Inicializa la colección ChromaDB con los archivos Markdown."""
    # Lista de archivos a procesar
    file_paths = [
        "mdFiles/ca.md",
        "mdFiles/en.md",
        "mdFiles/es.md",
        "mdFiles/index.md"
    ]

    # Eliminar colección existente para evitar duplicados
    try:
        chroma_client.delete_collection(collection_name)
        print(f"✅ Colección '{collection_name}' eliminada antes de insertar nuevos datos.")
    except:
        print(f"⚠️ La colección '{collection_name}' no existía.")

    # Crear nueva colección
    global collection
    collection = chroma_client.get_or_create_collection(name=collection_name)

    # Procesar archivos
    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                markdown_text = f.read()
            plain_text = md_to_text(markdown_text)
            chunks = chunk_text(plain_text)
            print(f"📄 Procesando archivo: {file_path}")
            for i, chunk in enumerate(chunks):
                collection.add(
                    ids=[f"{file_path}_chunk_{i}"],
                    documents=[chunk],
                    metadatas=[{"chunk_id": i, "source_file": file_path}],
                    embeddings=[compute_embedding(chunk)]
                )
            print(f"✅ Archivo {file_path} procesado y guardado en ChromaDB.\n")
        except Exception as e:
            print(f"⚠️ Error procesando el archivo {file_path}: {e}")

# Inicializar la colección al importar el módulo (solo se ejecuta una vez)
initialize_collection()

# Exportar variables y funciones necesarias
__all__ = ["compute_embedding", "collection"]