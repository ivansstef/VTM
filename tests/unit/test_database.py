"""
Unit tests for database operations
"""
import pytest
from app.models import Document, DocumentItem, StockBalance
from app import db, create_app

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_document():
    """Test document creation"""
    doc = Document(
        doc_type='прихід',
        doc_number='ПР-001',
        doc_date='2025-11-01'
    )
    assert doc.doc_type == 'прихід'
    assert doc.doc_number == 'ПР-001'

def test_document_items():
    """Test document items creation and validation"""
    doc = Document(doc_type='прихід')
    item = DocumentItem(
        item_name='Test Item',
        quantity=10,
        category=1
    )
    doc.items.append(item)
    assert len(doc.items) == 1
    assert doc.items[0].quantity == 10

def test_stock_balance():
    """Test stock balance calculations"""
    balance = StockBalance(
        item_name='Test Item',
        quantity=100,
        category=1
    )
    assert balance.quantity == 100
    
def test_category_validation():
    """Test category validation"""
    with pytest.raises(ValueError):
        DocumentItem(
            item_name='Test Item',
            quantity=10,
            category=6  # Should raise error - invalid category
        )
