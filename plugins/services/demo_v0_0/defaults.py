
from core.config import db
from .schemas import Course


data = [dict(id="ECO3", title="Economie 3"),
        dict(id="ECO4", title="Economie 4"),
        dict(id="INFO5", title="Informatique 5")]


def init_data():
    for row in data:
        course = Course(**row)
        db.session.merge(course)
    db.session.commit()

        