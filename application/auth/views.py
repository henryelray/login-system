from flask import render_template
from application.auth import login_bp


@login_bp.route('/')
def index():

    return render_template('auth/login.html')