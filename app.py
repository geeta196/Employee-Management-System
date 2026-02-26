from flask import Flask
from config import Config
from models import db
from routes import register_routes   # 👈 MUST import


from middleware import register_middleware
from errors import register_error_handlers
import os
import logging

app = Flask(__name__)
app.config.from_object(Config)

os.makedirs("logs", exist_ok=True)
os.makedirs("uploads", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)
register_middleware(app)
register_error_handlers(app)

# 👇 Route always before app.run
@app.route("/")
def home():
    logging.info("Home route accessed")
    return "Server Running"

if __name__ == "__main__":
    app.run(debug=True)