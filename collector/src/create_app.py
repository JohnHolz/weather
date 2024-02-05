from flask import Flask
from flask_cors import CORS
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
from routes.collector import collector_blueprint
from src.environment import get_secret_key, get_connection_string

def register_blueprints(app):
    app.register_blueprint(collector_blueprint)
    # limiter = Limiter(app, key_func=get_remote_address,
    #                   default_limits=["200 per day", "50 per hour"],
    #                   storage_uri="memory://",)
    # limiter.limit("20/minute")(user_blueprint)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = get_connection_string()
    app.config['SECRET_KEY'] = get_secret_key()

    CORS(app)
    register_blueprints(app)
    return app