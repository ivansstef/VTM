"""
VTM Project - Database Module
Created: November 1, 2025
Description: Handles database connections and configurations
"""

from flask import Flask
from flask_migrate import Migrate
from app.models import db

def init_db(app: Flask):
    """Initialize database connection"""
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vtm.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    
    return db, migrate

def init_test_db(app: Flask):
    """Initialize test database"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    return db
