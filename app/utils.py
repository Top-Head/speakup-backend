import json
from app import model, db
from app.models import Document

def chunk_text(text, chunk_size=300):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def save_document(title, url, text, source):
    for chunk in chunk_text(text):
        embedding = model.encode(chunk).tolist()
        doc = Document(
            title=title,
            url=url,
            text=chunk,
            embedding=json.dumps(embedding),
            source=source
        )
        db.session.add(doc)
    db.session.commit()