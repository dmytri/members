from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'  # Change this in production!
    
    # Initialize Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    
    # Register routes
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app