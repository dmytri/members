import pytest
import sys
from flask import Flask

sys.path.append("/srv")
from app import create_app

@pytest.fixture(autouse=True)
def app():
    # Set the test config before importing create_app
    Flask.test_config = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "TESTING": True,
        "WTF_CSRF_ENABLED": False
    }
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

