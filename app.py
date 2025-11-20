from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user
from auth import auth_blueprint
from models import db, User
from plagiarism_checker import plagiarism_blueprint
import os
from database import init_db

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(plagiarism_blueprint)

@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('plagiarism.admin_dashboard'))
        else:
            return redirect(url_for('plagiarism.user_dashboard'))
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    with app.app_context():
        init_db(app)
        os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)
