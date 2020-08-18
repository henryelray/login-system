from flask import Blueprint

login_bp = Blueprint('login_bp', __name__, template_folder='templates', static_folder='static'
                     )

