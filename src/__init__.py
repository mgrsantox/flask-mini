from flask import Flask
from os import environ
from . import config, users, routes
from .databse import db, migrate


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    flask_env = environ.get("FLASK_ENV", None)

    # Application Configuration

    if flask_env == "development":
        app.config.from_object(config.DevelopmentConfig)
    elif flask_env == "production":
        app.config.from_object(config.ProductionConfig)
    elif flask_env == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(routes.bp)
        app.register_blueprint(users.bp)
        return app
