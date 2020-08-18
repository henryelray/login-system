from flask import Flask

app = Flask(__name__)

from application.auth.views import login_bp

app.register_blueprint(login_bp)