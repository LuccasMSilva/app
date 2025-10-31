from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    CORS(app)

    from app.models import User, Clinica, Tutor, Animal

    from app.auth.routes import auth_bp
    from app.admin.routes import admin_bp
    from app.clinica.routes import clinica_bp
    from app.tutor.routes import tutor_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(clinica_bp)
    app.register_blueprint(tutor_bp)

    login_manager.login_view = 'auth.login'

    return app