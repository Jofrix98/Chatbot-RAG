import chromadb
from sentence_transformers import SentenceTransformer
import torch

# Cargar modelo de embeddings (elige un modelo eficiente)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Rápido y preciso

# Crear una función para generar embeddings sin OpenAI
def compute_embedding(text):
    return embedding_model.encode(text).tolist()