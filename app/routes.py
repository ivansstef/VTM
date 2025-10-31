"""
VTM Project - Routes Module
Created: November 1, 2025
Description: Contains all route definitions for the VTM application
"""

from flask import render_template, request, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html')
