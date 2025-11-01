"""
VTM Project - Configuration Module
Created: November 1, 2025
Description: Contains all configuration settings for the VTM application
"""

import os
from datetime import timedelta

# Base directory of the application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data', 'main.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Security
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-replace-in-production'
PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

# Backup
BACKUP_DIR = os.path.join(BASE_DIR, 'backup')
BACKUP_INTERVAL_DAYS = 7

# Application settings
UNIT_NAME = os.environ.get('UNIT_NAME') or 'ВЧ А2600'
YEAR_START = 2024

# Debug mode
DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')
