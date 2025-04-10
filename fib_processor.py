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

# Eliminar todos los documentos existentes en la colección en lotes
batch_size = 166  # Tamaño máximo permitido por ChromaDB
all_ids = collection.get()["ids"]
if all_ids:
    for i in range(0, len(all_ids), batch_size):
        batch_ids = all_ids[i:i + batch_size]
        collection.delete(ids=batch_ids)
        print(f"✅ Se eliminaron {len(batch_ids)} documentos del lote {i // batch_size + 1}.")
    print(f"✅ Se eliminaron todos los documentos de la colección.")
else:
    print("⚠️ No había documentos previos en la colección.")



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


# =========================================================================================
#                                       REALIZAR PREGUNTAS
# =========================================================================================
pregunta = input("Pregunta: " + " ")  # Mostramos la pregunta y capturamos la respuesta

inicio = "Eres un chatbot basado en la información de la FIB."
contexto_ini = "La respuesta a la pregunta que hará el usuario puede estar contenida en los siguiente textos separados por líeas horizontales.\n\n" # Guardamos la pregunta en una variable
query_text = input("Pregunta: ")  # Mostramos la pregunta y capturamos la respuesta

# Obtener embedding de la consulta
query_embedding = compute_embedding(query_text)

# Buscar en ChromaDB los fragmentos más relevantes
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=10
)
# Mostrar los resultados
contexto = ""
for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
    contexto += '--------------------\n' + "Con similitud a la pregunta = " + f"{dist}\n" + f"{doc}\n"

prompt = inicio + "\n\n" + contexto_ini + "\n\n" + contexto + "\n\n" + "Pregunta del usuario: " + query_text
print(prompt)
