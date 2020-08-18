from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from application.auth.views import login_bp

app.register_blueprint(login_bp)