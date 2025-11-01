"""
Unit tests for Flask application routes
"""
import pytest
from app import create_app
from flask import url_for

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    """Test home page access"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'VTM System' in response.data

def test_login_page(client):
    """Test login page access and form"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_protected_page(client):
    """Test access to protected page"""
    response = client.get('/documents')
    # Should redirect to login if not authenticated
    assert response.status_code == 302
    assert '/login' in response.location

def test_document_creation(client):
    """Test document creation route"""
    # Login first
    client.post('/login', data={
        'username': 'test',
        'password': 'test'
    })
    
    # Try to create document
    response = client.post('/documents/create', data={
        'doc_type': 'прихід',
        'doc_number': 'TEST-001',
        'items': [{'name': 'Test', 'quantity': 1}]
    })
    assert response.status_code == 200
