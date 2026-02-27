"""
Application factory for the HBnB API.

This module provides the Flask application factory used to create
and configure the application instance, initialize the REST API,
and register all namespaces.
"""


from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns


def create_app():
    """
    Create and configure the Flask application.

    This factory initializes the Flask app instance, sets up the
    Flask-RESTX API with metadata and documentation endpoint,
    and registers all API namespaces.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')

    return app
