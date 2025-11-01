"""
VTM Project - Reports Blueprint
Created: November 1, 2025
"""

from flask import Blueprint, render_template, send_file
from flask_login import login_required
from app.models import Document, StockBalance
import io

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/')
@login_required
def index():
    return render_template('reports/index.html')

@bp.route('/balance')
@login_required
def balance():
    balances = StockBalance.query.all()
    return render_template('reports/balance.html', balances=balances)

@bp.route('/documents')
@login_required
def documents():
    docs = Document.query.order_by(Document.date.desc()).all()
    return render_template('reports/documents.html', documents=docs)

@bp.route('/annex32')
@login_required
def annex32():
    return render_template('reports/annex32.html')

@bp.route('/annex1')
@login_required
def annex1():
    return render_template('reports/annex1.html')

@bp.route('/annex2')
@login_required
def annex2():
    return render_template('reports/annex2.html')
