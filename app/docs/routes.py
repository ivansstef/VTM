"""
VTM Project - Documents Blueprint
Created: November 1, 2025
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import Document

bp = Blueprint('docs', __name__, url_prefix='/docs')

@bp.route('/')
@login_required
def index():
    documents = Document.query.order_by(Document.date.desc()).all()
    return render_template('docs/index.html', documents=documents)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        # Minimal handling: expect number and doc_type in form (if provided)
        number = request.form.get('number')
        doc_type = request.form.get('doc_type')
        # In future: validate and save to DB
        flash('Документ створено (тимчасово, без збереження).', 'success')
        return redirect(url_for('docs.index'))
    return render_template('docs/create.html')

@bp.route('/import-stock', methods=['GET', 'POST'])
@login_required
def import_stock():
    from app.models import Service
    services = Service.query.filter_by(is_active=True).order_by(Service.name).all()
    if request.method == 'POST':
        # Minimal handling: accept service id and file presence
        service_id = request.form.get('service')
        file = request.files.get('file')
        if not service_id or not file:
            flash('Оберіть службу та файл.', 'danger')
            return redirect(url_for('docs.import_stock'))
        # In future: process Excel file and update balances
        flash('Файл завантажено (тимчасово, обробка не реалізована).', 'success')
        return redirect(url_for('docs.index'))
    return render_template('docs/import_stock.html', services=services)

@bp.route('/<int:id>')
@login_required
def view(id):
    document = Document.query.get_or_404(id)
    return render_template('docs/view.html', document=document)
