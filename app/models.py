"""
VTM Project - Models Module
Created: November 1, 2025
Description: Contains database models and schema definitions
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """Користувачі системи"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Service(db.Model):
    """Довідник служб"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    
    # Зв'язки
    balances = db.relationship('StockBalance', back_populates='service')
    documents = db.relationship('Document', back_populates='service')

class Supplier(db.Model):
    """Довідник постачальників/отримувачів"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(300))
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    is_active = db.Column(db.Boolean, default=True)
    
    # Зв'язки
    documents_from = db.relationship('Document', back_populates='supplier_from', foreign_keys='Document.supplier_from_id')
    documents_to = db.relationship('Document', back_populates='supplier_to', foreign_keys='Document.supplier_to_id')

class Document(db.Model):
    """Головна таблиця документів"""
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), nullable=False, index=True)
    date = db.Column(db.Date, nullable=False, index=True)
    doc_type = db.Column(db.String(20), nullable=False)  # накладна, акт, тощо
    status = db.Column(db.String(20), nullable=False, default='draft')  # draft, active, cancelled
    
    # Зв'язки з довідниками
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    supplier_from_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    supplier_to_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    
    # Зворотні зв'язки
    service = db.relationship('Service', back_populates='documents')
    supplier_from = db.relationship('Supplier', back_populates='documents_from', foreign_keys=[supplier_from_id])
    supplier_to = db.relationship('Supplier', back_populates='documents_to', foreign_keys=[supplier_to_id])
    items = db.relationship('DocumentItem', back_populates='document', cascade='all, delete-orphan')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    __table_args__ = (
        db.Index('idx_document_number_date', 'number', 'date'),
    )

class DocumentItem(db.Model):
    """Позиції в документах"""
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Numeric(10, 3), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Numeric(10, 2))
    
    # Зв'язки
    document = db.relationship('Document', back_populates='items')
    
    __table_args__ = (
        db.Index('idx_document_item_code', 'code'),
    )

class StockBalance(db.Model):
    """Залишки по службах"""
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    item_code = db.Column(db.String(50), nullable=False)
    item_name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Numeric(10, 3), nullable=False, default=0)
    unit = db.Column(db.String(10), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Зв'язки
    service = db.relationship('Service', back_populates='balances')
    
    __table_args__ = (
        db.UniqueConstraint('service_id', 'item_code', name='uq_stock_balance_service_item'),
        db.Index('idx_stock_balance_item', 'item_code'),
    )

class AuditLog(db.Model):
    """Журнал дій користувачів"""
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action = db.Column(db.String(50), nullable=False)
    table_name = db.Column(db.String(50), nullable=False)
    record_id = db.Column(db.Integer)
    details = db.Column(db.Text)
    
    __table_args__ = (
        db.Index('idx_audit_log_timestamp', 'timestamp'),
        db.Index('idx_audit_log_user', 'user_id'),
    )
