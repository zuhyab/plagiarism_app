from werkzeug.security import generate_password_hash
from models import db, User
import os

DEFAULT_ADMIN_USERNAME = os.environ.get("PLAG_ADMIN_USER", "admin")
DEFAULT_ADMIN_PASSWORD = os.environ.get("PLAG_ADMIN_PASS", "admin123")

def init_db(app):
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(username=DEFAULT_ADMIN_USERNAME).first()
        if not admin:
            hashed = generate_password_hash(DEFAULT_ADMIN_PASSWORD)
            admin_user = User(username=DEFAULT_ADMIN_USERNAME, password=hashed, is_admin=True)
            db.session.add(admin_user)
            db.session.commit()
            print(f"[database] Created default admin account -> {DEFAULT_ADMIN_USERNAME}:{DEFAULT_ADMIN_PASSWORD}")
        else:
            print("[database] Admin account exists, skipping creation.")
from werkzeug.security import generate_password_hash
from models import db, User
import os

DEFAULT_ADMIN_USERNAME = os.environ.get("PLAG_ADMIN_USER", "admin")
DEFAULT_ADMIN_PASSWORD = os.environ.get("PLAG_ADMIN_PASS", "admin123")

def init_db(app):
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(username=DEFAULT_ADMIN_USERNAME).first()
        if not admin:
            hashed = generate_password_hash(DEFAULT_ADMIN_PASSWORD)
            admin_user = User(username=DEFAULT_ADMIN_USERNAME, password=hashed, is_admin=True)
            db.session.add(admin_user)
            db.session.commit()
            print(f"[database] Default admin created -> {DEFAULT_ADMIN_USERNAME}:{DEFAULT_ADMIN_PASSWORD}")
        else:
            print("[database] Admin account exists.")
