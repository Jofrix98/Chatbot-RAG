from flask import Flask, request, jsonify
from fib_processor import compute_embedding, collection  # Importa desde fib_processor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "No se proporcionó una pregunta"}), 400

    # Obtener embedding de la consulta
    query_embedding = compute_embedding(question)

    # Buscar en ChromaDB los fragmentos más relevantes
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    # Construir el contexto de respuesta
    contexto = ""
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        contexto += '--------------------\n' + f"Con similitud a la pregunta = {dist}\n{doc}\n"

    # Respuesta final
    respuesta = {
        "contexto": contexto,
        "pregunta": question
    }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)