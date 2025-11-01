"""
VTM Project - Documents Module
Created: November 1, 2025
Description: Blueprint for document management functionality
"""

from flask import Blueprint

documents_bp = Blueprint('documents', __name__, url_prefix='/documents')

from app.documents import routes