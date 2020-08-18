from application import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

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