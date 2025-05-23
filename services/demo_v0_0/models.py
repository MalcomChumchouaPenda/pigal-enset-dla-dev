
from core.config import db


class Course(db.Model):
    __bind_key__ = 'courses_v0'
    id = db.Column(db.String(15), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    