"""
VTM Project - API Blueprint
Created: November 1, 2025
"""

from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Document, Service, Supplier, StockBalance

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/documents')
@login_required
def get_documents():
    documents = Document.query.all()
    return jsonify([{
        'id': doc.id,
        'number': doc.number,
        'date': doc.date.isoformat(),
        'type': doc.doc_type,
        'status': doc.status
    } for doc in documents])

@bp.route('/services')
@login_required
def get_services():
    services = Service.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'code': s.code
    } for s in services])

@bp.route('/balance/<service_code>')
@login_required
def get_balance(service_code):
    service = Service.query.filter_by(code=service_code).first_or_404()
    balances = StockBalance.query.filter_by(service_id=service.id).all()
    return jsonify([{
        'item_code': b.item_code,
        'item_name': b.item_name,
        'quantity': float(b.quantity),
        'unit': b.unit
    } for b in balances])
