from config.config import init_app
from flask import Flask


def create_app():
    app = Flask(__name__)
    init_app(app)
    return app
