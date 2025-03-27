import chromadb
from sentence_transformers import SentenceTransformer
import torch
import markdown
from bs4 import BeautifulSoup

# Cargar modelo de embeddings (elige un modelo eficiente)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Rápido y preciso

# Crear una función para generar embeddings sin OpenAI
def compute_embedding(text):
    return embedding_model.encode(text).tolist()

# Cliente con persistencia en Colab
chroma_client = chromadb.PersistentClient(path="/content/chromadb_data")

# Eliminar la colección si ya existe
collection_name = "fib_web_data"

# Obtener la colección (sin eliminarla completamente)
collection = chroma_client.get_or_create_collection(name=collection_name)

# Eliminar todos los documentos existentes en la colección
all_ids = collection.get()["ids"]
if all_ids:
    collection.delete(ids=all_ids)
    print(f"✅ Se eliminaron {len(all_ids)} documentos de la colección.")
else:
    print("⚠️  No había documentos previos en la colección.")



# 🔹 Lista de archivos a procesar
file_paths = [
    "mdFiles/ca.md",
    "mdFiles/en.md",
    "mdFiles/es.md",
    "mdFiles/index.md"
]

# 🔹 Configurar ChromaDB
chroma_client = chromadb.PersistentClient(path="/content/chromadb_data")
collection_name = "fib_web_data"

# 🔹 Eliminar la colección si ya existe para evitar duplicados
try:
    chroma_client.delete_collection(collection_name)
    print(f"✅ Colección '{collection_name}' eliminada antes de insertar nuevos datos.")
except:
    print(f"⚠️ La colección '{collection_name}' no existía.")

# 🔹 Crear una nueva colección limpia
collection = chroma_client.get_or_create_collection(name=collection_name)

# 🔹 Cargar modelo de embeddings local
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_embedding(text):
    """Genera embeddings para el texto usando Sentence Transformers."""
    return embedding_model.encode(text).tolist()

def chunk_text(text, chunk_size=200, overlap=25):
    """
    Divide el texto en fragmentos de tamaño 'chunk_size' con un solapamiento 'overlap'.
    Garantiza que el solapamiento sea efectivo incluso en los últimos fragmentos.
    """
    chunks = []
    start = 0
    num_chunks = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))  # Asegura que no exceda el tamaño total
        chunk = text[start:end]

        # Evitar fragmentos vacíos en los últimos trozos del texto
        if chunk:
            chunks.append(chunk)
            num_chunks += 1

        start += chunk_size - overlap  # Desplazamiento con solapamiento

    print(f"✅ Número de fragmentos generados: {num_chunks} para este archivo.")
    return chunks

def md_to_text(md_content):
    """Convierte Markdown a texto plano sin etiquetas HTML."""
    html = markdown.markdown(md_content)  # Convierte Markdown a HTML
    soup = BeautifulSoup(html, "html.parser")  # Elimina etiquetas HTML
    return soup.get_text()

# 🔹 Procesar múltiples archivos
for file_path in file_paths:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_text = f.read()

        # Convertir Markdown a texto limpio
        plain_text = md_to_text(markdown_text)

        # Dividir en chunks con overlapping
        chunks = chunk_text(plain_text)

        print(f"📄 Procesando archivo: {file_path}")

        # Agregar los fragmentos con embeddings a ChromaDB
        for i, chunk in enumerate(chunks):
            collection.add(
                ids=[f"{file_path}_chunk_{i}"],  # ID único basado en el nombre del archivo
                documents=[chunk],
                metadatas=[{"chunk_id": i, "source_file": file_path}],
                embeddings=[compute_embedding(chunk)]
            )

        print(f"✅ Archivo {file_path} procesado y guardado en ChromaDB.\n")

    except Exception as e:
        print(f"⚠️ Error procesando el archivo {file_path}: {e}")