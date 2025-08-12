from app import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    url = db.Column(db.String(500))
    text = db.Column(db.Text)
    embedding = db.Column(db.Text) 
    source = db.Column(db.String(50)) 