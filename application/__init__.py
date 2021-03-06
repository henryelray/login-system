from flask import Flask
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from application.auth import models
from application.auth.views import login_bp

app.register_blueprint(login_bp)