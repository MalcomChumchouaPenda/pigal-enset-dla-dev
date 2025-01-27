
from datetime import datetime as dt
from core.utils import get_store
from . import schemas as sch


TIME_EXP = r'%d/%m/%Y'
store = get_store('demo')


def init_categories(session):
    records = store.read_json('samples/event_categories.json')
    for record in records:
        obj = sch.Category(**record)
        session.merge(obj)
    session.commit()

def init_events(session):
    records = store.read_json('samples/events.json')
    for record in records:
        record['date'] = dt.strptime(record['date'], TIME_EXP)
        obj = sch.Event(**record)
        session.merge(obj)
    session.commit()

def init_pays(session):
    records = store.read_json('samples/pays.json')
    for record in records:
        obj = sch.Pays(**record)
        session.merge(obj)
    session.commit()

def init_professions(session):
    records = store.read_json('samples/professions.json')
    for record in records:
        obj = sch.Profession(**record)
        session.merge(obj)
    session.commit()

def init_formations(session):
    records = store.read_json('samples/formations.json')
    for record in records:
        obj = sch.Formation(**record)
        session.merge(obj)
    session.commit()

def init_departments(session):
    records = store.read_json('samples/departments.json')
    for record in records:
        obj = sch.Department(**record)
        session.merge(obj)
    session.commit()

def init_labs(session):
    records = store.read_json('samples/labs.json')
    for record in records:
        obj = sch.Lab(**record)
        session.merge(obj)
    session.commit()

def init_levels(session):
    records = store.read_json('samples/levels.json')
    for record in records:
        obj = sch.Level(**record)
        session.merge(obj)
    session.commit()

def init_diplomas(session):
    records = store.read_json('samples/diplomas.json')
    for record in records:
        obj = sch.Diploma(**record)
        session.merge(obj)
    session.commit()

def init_options(session):
    records = store.read_json('samples/options.json')
    for record in records:
        obj = sch.Option(**record)
        session.merge(obj)
    session.commit()

def init_courses(session):
    records = store.read_json('samples/courses.json')
    for record in records:
        obj = sch.Course(**record)
        session.merge(obj)
    session.commit()