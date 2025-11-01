"""
VTM Project - App Initialization
Created: November 1, 2025
Description: Flask application initialization and configuration
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_object=None):
    app = Flask(__name__)
    
    # Load config
    if config_object is None:
        app.config.from_object('config')
    else:
        app.config.from_object(config_object)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    return app

# Create the app instance
app = create_app()

# Import routes after app creation to avoid circular imports
from app import routes
