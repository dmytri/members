import os
import sys


from flask.cli import FlaskGroup
from . import create_app

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        # For test database, just create tables directly
        if 'sqlite:///:memory:' in app.config['SQLALCHEMY_DATABASE_URI']:
            from app.models import db
            db.create_all()
        # For real database, handle migrations
        else:
            migrations_dir = os.path.join(os.path.dirname(__file__), '..', 'migrations')
            alembic_ini = os.path.join(migrations_dir, 'alembic.ini')
            
            from flask_migrate import init, migrate, upgrade
        
            if not os.path.exists(alembic_ini):
                init()
            migrate(message='Auto-migration')
            upgrade()
