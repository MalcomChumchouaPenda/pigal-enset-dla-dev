
from core.config import db


CASCADE = "all, delete-orphan"


class Event(db.Model):    
    __bind_key__ = 'demo'
    __tablename__ = 'events'
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    level = db.Column(db.Integer, default=0)
    category_id = db.Column(db.String, db.ForeignKey('categories.id'))

class Category(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'categories'
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    events = db.relationship('Event', backref='category', cascade=CASCADE)


class Pays(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'pays'
    id = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    group = db.Column(db.String(150), nullable=True)

class Profession(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'profession'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

