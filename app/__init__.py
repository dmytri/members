import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate, init, migrate, upgrade
from app.models import db

login_manager = LoginManager()
migrate_extension = Migrate()

def init_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    
    # Apply test config if it exists
    if hasattr(Flask, 'test_config'):
        app.config.update(Flask.test_config)
        delattr(Flask, 'test_config')
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
    if 'SQLALCHEMY_DATABASE_URI' not in app.config:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    print("\nDatabase URI check:")
    print(f"  Current URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"  Is memory database: {'sqlite:///:memory:' in app.config['SQLALCHEMY_DATABASE_URI']}\n")
    
    # Initialize extensions
    db.init_app(app)
    migrate_extension.init_app(app, db)
    init_login_manager(app)
    
    # Initialize database
    with app.app_context():
        if 'sqlite:///:memory:' in app.config['SQLALCHEMY_DATABASE_URI']:
            print("Test database detected - creating tables directly")
            db.create_all()
        else:
            migrations_dir = os.path.join(os.path.dirname(__file__), '..', 'migrations')
            alembic_ini = os.path.join(migrations_dir, 'alembic.ini')
            
            if not os.path.exists(alembic_ini):
                print("No migrations found - initializing...")
                init()
                print("Creating initial migration...")
                migrate(message='Initial migration')
                print("Applying initial migration...")
                upgrade()
            else:
                print("Creating new migration...")
                migrate(message='Auto-migration')
                print("Applying new migration...")
                upgrade()
            
            print("Database initialization complete\n")
    
    # Register routes
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app