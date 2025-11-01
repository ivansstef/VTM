"""
VTM Project - Documents Routes
"""

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Document
from app.database import db
from datetime import datetime
from app.documents import documents_bp as bp

@bp.route('/')
@login_required
def index():
    documents = Document.query.order_by(Document.date.desc()).all()
    return render_template('documents/document_list.html', documents=documents)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        document = Document(
            number=request.form['number'],
            date=datetime.strptime(request.form['date'], '%Y-%m-%d').date(),
            sender=request.form['sender'],
            receiver=request.form['receiver'],
            description=request.form['description'],
            created_by_id=current_user.id
        )
        db.session.add(document)
        try:
            db.session.commit()
            flash('Накладну успішно створено', 'success')
            return redirect(url_for('documents.index'))
        except:
            db.session.rollback()
            flash('Помилка при створенні накладної', 'error')
    
    return render_template('documents/create.html')

@bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    document = Document.query.get_or_404(id)
    
    if request.method == 'POST':
        document.number = request.form['number']
        document.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        document.sender = request.form['sender']
        document.receiver = request.form['receiver']
        document.description = request.form['description']
        
        try:
            db.session.commit()
            flash('Накладну успішно оновлено', 'success')
            return redirect(url_for('documents.index'))
        except:
            db.session.rollback()
            flash('Помилка при оновленні накладної', 'error')
    
    return render_template('documents/create.html', document=document)

@bp.route('/<int:id>')
@login_required
def view(id):
    document = Document.query.get_or_404(id)
    return render_template('documents/view.html', document=document)

@bp.route('/import-stock', methods=['GET', 'POST'])
@login_required
def import_stock():
    from app.models import Service
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не вибрано файл', 'error')
            return redirect(request.url)
            
        file = request.files['file']
        service_id = request.form.get('service_id')
        
        if file.filename == '':
            flash('Не вибрано файл', 'error')
            return redirect(request.url)
            
        if not service_id:
            flash('Не вибрано службу', 'error')
            return redirect(request.url)
            
        # TODO: Додати логіку імпорту
        flash('Функція імпорту в розробці', 'info')
        return redirect(url_for('documents.index'))
    
    services = Service.query.all()
    return render_template('documents/import_stock.html', services=services)
