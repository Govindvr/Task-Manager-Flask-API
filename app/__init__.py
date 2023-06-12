from flask import Flask
from flask_restful import Api
from config import Config
from .models import db
from .routes import UserResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register API resources
    api = Api(app)
    api.add_resource(UserResource, '/users')

    return app