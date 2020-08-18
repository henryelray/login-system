from application import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(68), index=True, unique=True)
    password_hash = db.Column(db.String(80), index=True, unique=True)

    def __repr__(self):

        return '<User> {}'.format(self.username)