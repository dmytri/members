from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, email):
        self.email = email
        self.password_hash = None
        
    def get_id(self):
        return self.email
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Simple in-memory user store (replace with database in production)
users = {}

def get_user(email):
    return users.get(email)