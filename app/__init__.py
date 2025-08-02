from flask import Flask
from .shortener import shortener_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(shortener_bp)
    return app