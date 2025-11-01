"""
VTM Project - Documents Blueprint
Created: November 1, 2025
"""

from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Document

bp = Blueprint('docs', __name__, url_prefix='/docs')

@bp.route('/')
@login_required
def index():
    documents = Document.query.order_by(Document.date.desc()).all()
    return render_template('docs/list.html', documents=documents)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    return render_template('docs/create.html')

@bp.route('/import-stock', methods=['GET', 'POST'])
@login_required
def import_stock():
    from app.models import Service
    services = Service.query.filter_by(is_active=True).order_by(Service.name).all()
    return render_template('docs/import_stock.html', services=services)

@bp.route('/<int:id>')
@login_required
def view(id):
    document = Document.query.get_or_404(id)
    return render_template('docs/view.html', document=document)
