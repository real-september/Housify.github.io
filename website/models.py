from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class eState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String())
    area = db.Column(db.String())
    location = db.Column(db.String())
    status = db.Column(db.String())
    age = db.Column(db.Integer())
    size = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(150))
    estates = db.relationship('eState')