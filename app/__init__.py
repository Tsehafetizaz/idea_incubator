# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints here

    return app
