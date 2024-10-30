from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, users, get_user
from app import login_manager

bp = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(email):
    return get_user(email)

@bp.route('/')
@bp.route('/home')
@login_required
def home():
    return render_template('shell.html', page='home')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user(email)
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.home'))
        flash('Invalid email or password')
    
    return render_template('shell.html', page='login')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in users:
            flash('Email already registered')
        else:
            user = User(email)
            user.set_password(password)
            users[email] = user
            login_user(user)
            return redirect(url_for('main.home'))
            
    return render_template('shell.html', page='register')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@bp.route('/content/<page>')
def content(page):
    return render_template(f'{page}.html')