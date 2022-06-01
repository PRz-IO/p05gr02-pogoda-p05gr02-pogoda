from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail #pip install Flask-Mail
from apscheduler.schedulers.background import BackgroundScheduler    #pip install apscheduler


db = SQLAlchemy()
DB_NAME = "database.db"

mail = Mail()

def create_app():
    app = Flask(__name__, static_folder='./static')
    app.config['SECRET_KEY'] = "gflgkdfgdfgogsdfksdflsdsfkgekh"
    #app.config['SQLALCHEMY_ECHO'] = True   #wypisuje sql
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'aplikacjapogodowa2022@gmail.com'
    app.config['MAIL_PASSWORD'] = 'HasloApkaPogodowa1!'
    app.config['MAIL_DEFAULT_SENDER'] = ('Aplikacja Pogodowa', 'aplikacjapogodowa2022@gmail.com')
    app.config['MAIL_ASSCII_ATTACHMENTS'] = False
    app.config['MAIL_SUPRESS_SEND'] = False



    # db init
    db.init_app(app)

    # mail init
    mail.init_app(app)

    # blue prints
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    # models
    from .models import User
    from .przyklad import zaladuj_przyklad, dodaj
    from .codziennePowiadomienie import powiadomieniePogodowe
    # database startup
    create_database(app)

    # login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    #zaladuj_przyklad(app, db)
    #dodaj(app,db)

    sched = BackgroundScheduler(daemon=True)
    sched.add_job(powiadomieniePogodowe, 'cron', day='*', hour=8, minute=30, args=(app, db)) #każdego dnia o godzinie 8:30 wykonuje funkcję
    sched.start()


    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("[DB] Created database")
