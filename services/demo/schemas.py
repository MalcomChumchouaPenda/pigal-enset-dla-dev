
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
    __tablename__ = 'professions'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Formation(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'formations'
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    options = db.relationship('Option', backref='formation', cascade=CASCADE)

class Unit(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'units'
    __mapper_args__ = {
        "polymorphic_identity": "units",
        "polymorphic_on": "type",
    }
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    text = db.Column(db.String(200), nullable=True)
    type = db.Column(db.String(200))
    options = db.relationship('Option', backref='unit', cascade=CASCADE)

class Department(Unit):
    __bind_key__ = 'demo'
    __tablename__ = 'departments'
    __mapper_args__ = {"polymorphic_identity": "departments"}
    id = db.Column(db.String(50), db.ForeignKey('units.id'), primary_key=True)
    
class Lab(Unit):
    __bind_key__ = 'demo'
    __tablename__ = 'labs'
    __mapper_args__ = {"polymorphic_identity": "labs"}
    id = db.Column(db.String(50), db.ForeignKey('units.id'), primary_key=True)

class Level(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'levels'
    id = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', backref='level', cascade=CASCADE)
    
class Diploma(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'diplomas'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    abbr = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Course', backref='diploma', cascade=CASCADE)

class Option(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'options'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unit_id = db.Column(db.String(50), db.ForeignKey('units.id'))
    formation_id = db.Column(db.String(5), db.ForeignKey('formations.id'))
    courses = db.relationship('Course', backref='option', cascade=CASCADE)

class Course(db.Model):
    __bind_key__ = 'demo'
    __tablename__ = 'courses'
    id = db.Column(db.String(10), primary_key=True)
    open = db.Column(db.Boolean, nullable=False)
    period = db.Column(db.String(9), nullable=False)
    text = db.Column(db.String(200), nullable=True)
    option_id = db.Column(db.String(10), db.ForeignKey('options.id'))
    diploma_id = db.Column(db.String(10), db.ForeignKey('diplomas.id'))
    level_id = db.Column(db.String(15), db.ForeignKey('levels.id'))
