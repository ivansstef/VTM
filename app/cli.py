"""
VTM Project - CLI Commands
Created: November 1, 2025
"""

import click
from flask.cli import with_appcontext
from app.models import db, User, Service, Supplier

@click.command('create-admin')
@click.argument('username')
@click.argument('email')
@click.argument('password')
@with_appcontext
def create_admin_command(username, email, password):
    """Create a new admin user."""
    try:
        if User.query.filter_by(username=username).first():
            click.echo(f'Error: User {username} already exists.')
            return
            
        user = User(
            username=username,
            email=email,
            is_active=True
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f'Admin user {username} created successfully.')
    except Exception as e:
        click.echo(f'Error creating admin user: {str(e)}')
        db.session.rollback()

@click.command('test-db')
@with_appcontext
def test_db_command():
    """Test database connection and models."""
    try:
        # Clean up any existing test data
        User.query.filter_by(username="test_user").delete()
        Service.query.filter_by(code="TEST-01").delete()
        Supplier.query.filter_by(code="SUP-01").delete()
        db.session.commit()
        
        # Create test user
        user = User(username="test_user", email="test@example.com")
        user.set_password("test123")
        db.session.add(user)
        
        # Create test service
        service = Service(name="Test Service", code="TEST-01")
        db.session.add(service)
        
        # Create test supplier
        supplier = Supplier(
            name="Test Supplier",
            code="SUP-01",
            contact_person="John Doe",
            phone="123456789"
        )
        db.session.add(supplier)
        
        # Commit changes
        db.session.commit()
        
        # Verify data
        print("\n✅ Database check results:")
        print(f"User created: {User.query.filter_by(username='test_user').first().username}")
        print(f"Service created: {Service.query.filter_by(code='TEST-01').first().name}")
        print(f"Supplier created: {Supplier.query.filter_by(code='SUP-01').first().name}")
        
        # Cleanup
        db.session.delete(user)
        db.session.delete(service)
        db.session.delete(supplier)
        db.session.commit()
        print("\n🧹 Test data cleaned up successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during database test: {str(e)}")
        db.session.rollback()
        raise e
