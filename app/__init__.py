from flask import Flask, Blueprint
from .config import Config
from app.page.routes import page
from datetime import datetime
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(page)

    @app.context_processor
    def inject_current_year():
        return {"current_year": datetime.now().year}

    # with app.app_context():
    #     create_db()
    return app

