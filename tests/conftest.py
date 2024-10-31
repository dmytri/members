import pytest
import sys
sys.path.append('/srv')
from app import create_app
from app.models import db

@pytest.fixture(autouse=True)
def setup_test_db():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.drop_all() 