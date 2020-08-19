from flask import render_template, redirect, url_for, flash
from application.auth import login_bp
from application.auth.forms import LoginForm
from application.auth.models import User
from flask_login import login_user, current_user


@login_bp.route('/index')
def index():
    return render_template('index.html')


@login_bp.route('/', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:

        return redirect(url_for('login_bp.index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login_bp.index'))
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('login_bp.index'))

    return render_template('auth/login.html', form=form)
