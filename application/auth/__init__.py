from flask import Blueprint

login_bp = Blueprint('login_bp', __name__, template_folder='templates', static_folder='static',
                     static_url_path='/auth/static/css/styles.css'
                     )

