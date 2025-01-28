
from flask_login import UserMixin
from core.config import db


user_roles = db.Table(
    'user_roles',
    db.Column('user_id', db.String(25), db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.String(25), db.ForeignKey('role.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.String(25), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    roles = db.relationship('Role', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))

class Role(db.Model):
    id = db.Column(db.String(25), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
