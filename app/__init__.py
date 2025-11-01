"""
VTM Project - App Initialization
Created: November 1, 2025
Description: Flask application initialization and configuration
"""

import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from app.config import config
from app.database import init_db
from app.models import User
from app.cli import test_db_command, create_admin_command

# Initialize Flask extensions
login_manager = LoginManager()
csrf = CSRFProtect()
session = Session()

def create_app(config_name='default'):
    """Create and configure Flask application"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app) if hasattr(config[config_name], 'init_app') else None
    
    # Initialize database and migrations
    db, migrate = init_db(app)
    
    # Initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Будь ласка, увійдіть для доступу до цієї сторінки.'
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    # Initialize other extensions
    csrf.init_app(app)
    session.init_app(app)
    
    # Register CLI commands
    app.cli.add_command(test_db_command)
    app.cli.add_command(create_admin_command)
    # Register blueprints
    from app.auth import auth_bp
    from app.docs import docs_bp
    from app.reports import reports_bp
    from app.api import api_bp
    from app.main import main_bp
    
    app.register_blueprint(main_bp)  # Реєструємо першим, бо він обробляє корінь '/'
    app.register_blueprint(auth_bp)
    app.register_blueprint(docs_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(api_bp)
    
    # Configure logging
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/vtm.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        
        app.logger.setLevel(logging.INFO)
        app.logger.info('VTM startup')
    
    return app

# Create the app instance
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
