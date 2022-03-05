import os
from flask import Flask, current_app
from .routes import routes_bp as routes_blueprint


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    with app.app_context():
        app.register_blueprint(routes_blueprint)

    return app


