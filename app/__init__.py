from flask import Flask

from app.extensions import db, login_manager, bcrypt
from app.models import User
from app.main.routes import main_bp
from app.users.routes import users_bp
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "users.login"
    login_manager.login_message_category = "info"
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)

    return app
