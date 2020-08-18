from flask import render_template
from application.auth import login_bp
from .forms import LoginForm


@login_bp.route('/')
def index():
    form = LoginForm()
    return render_template('auth/login.html', form=form)