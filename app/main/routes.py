"""
VTM Project - Main Blueprint
Created: November 1, 2025
"""

from flask import Blueprint, render_template, request
from flask_login import login_required

bp = Blueprint('main', __name__)

from app.models import Document, Service, Supplier

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    stats = {
        'documents': Document.query.count(),
        'services': Service.query.count(),
        'suppliers': Supplier.query.count(),
        'recent_docs': Document.query.order_by(Document.created_at.desc()).limit(5).all()
    }
    
    return render_template('main/index.html', stats=stats)

@bp.route('/references')
@login_required
def references():
    ref_type = request.args.get('type', 'services')
    if ref_type == 'services':
        items = Service.query.all()
        title = 'Служби'
    else:
        items = Supplier.query.all()
        title = 'Постачальники'
    
    return render_template('main/references.html', items=items, title=title, type=ref_type)
