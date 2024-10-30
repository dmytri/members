from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from app.models import db

login_manager = LoginManager()
migrate = Migrate()

def init_login_manager(app):
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'  # Change this in production!
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    init_login_manager(app)
    
    # Register routes
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app