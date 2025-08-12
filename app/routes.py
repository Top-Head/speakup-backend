import json
from app import app, model
from app.models import Document
from flask import request, jsonify
from sentence_transformers import util
from app.service import fetch_core_articles, fetch_wikiquote_quotes

@app.route("/api/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Campo 'query' é obrigatório"}), 400

    query_embedding = model.encode(query)
    results = []

    for doc in Document.query.all():
        doc_embedding = json.loads(doc.embedding)
        score = util.cos_sim(query_embedding, doc_embedding).item()
        results.append({
            "title": doc.title,
            "url": doc.url,
            "text": doc.text,
            "score": score,
            "source": doc.source
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    if not results or results[0]["score"] < 0.4:
        print(f"[INFO] Nenhum resultado relevante, buscando online...")
        fetch_core_articles(query=query, limit=10)
        fetch_wikiquote_quotes(topic=query, limit=5)
        
        return search()

    return jsonify(results[:10])