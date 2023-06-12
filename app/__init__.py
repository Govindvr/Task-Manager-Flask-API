from flask import Flask
from flask_restful import Api
from config import Config
from .models import db
from .routes import initialise_routes
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Initialize flask-migrate
    migrate = Migrate(app, db)

    # Register API resources
    api = Api(app)
    initialise_routes(api)

    return app