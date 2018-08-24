from flask import Flask
from flask_mail import Mail
from app.models.base import db
from flask_login import LoginManager
# from app.models.book import db
# from app.models.user import db

login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)
    login_manager.init_app(app)
    mail.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册！'
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    from app.web.main import web
    from app.web.drift import web
    from app.web.gift import web
    from app.web.wish import web
    from app.web.auth import web
    app.register_blueprint(web)
