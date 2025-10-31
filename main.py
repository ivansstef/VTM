"""
VTM Project - Main Application Entry Point
Created: November 1, 2025
Description: Flask application initialization and configuration
"""

from flask import Flask
from app.database import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)
