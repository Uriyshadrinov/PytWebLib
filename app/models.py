# models.py
from app import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
