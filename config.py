# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/employee_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False