# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    position = db.Column(db.String(100))
    salary = db.Column(db.Float)
    image = db.Column(db.String(200))