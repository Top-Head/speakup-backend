import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sentence_transformers import SentenceTransformer

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///documents.db"

CORS(app)
db = SQLAlchemy(app)
model = SentenceTransformer("all-MiniLM-L6-v2")

CORE_API_URL = "https://api.core.ac.uk/v3/search/works"
CORE_API_KEY = "4keZU1VzhTXf3gHtwFQG5OYoInqrCuLv"

from app import routes