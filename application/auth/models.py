from flask_login import UserMixin

from application import db, login
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(68), index=True, unique=True)
    username = db.Column(db.String(68), index=True, unique=True)
    password_hash = db.Column(db.String(80), index=True, unique=True)

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)

    def __repr__(self):

        return '<User> {}'.format(self.username)


@login.user_loader
def load_user(id):

    return User.query.get(int(id))