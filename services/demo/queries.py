
from datetime import datetime as dt
from core.utils import get_store
from . import schemas as sch


TIME_EXP = r'%d/%m/%Y'
store = get_store('demo')


def init_data(session):
    init_categories(session)
    init_events(session)
    init_pays(session)
    init_professions(session)
    init_formations(session)
    init_departments(session)
    init_labs(session)
    init_levels(session)
    init_diplomas(session)
    init_options(session)
    init_courses(session)

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


def get_pays(session):
    query = session.query(sch.Pays)
    return query.all()

def get_professions(session):
    query = session.query(sch.Profession)
    return query.all()


def get_events(session, level=None):
    query = session.query(sch.Event)
    if level is not None:
        query = query.filter_by(level=level)
    return query.all()

def get_event(session, id):
    query = session.query(sch.Event)
    query = query.filter_by(id=id)
    return query.one()


def get_departments(session):
    query = session.query(sch.Department)
    return query.all()

def get_formations(session):
    query = session.query(sch.Formation)
    return query.all()

def get_labs(session):
    query = session.query(sch.Lab)
    return query.all()

def get_diplomas(session):
    query = session.query(sch.Diploma)
    return query.all()

def get_options(session, formation=None, unit=None):
    query = session.query(sch.Option)
    if formation:
        query = query.filter_by(formation_id=formation)
    if unit:
        query = query.filter_by(unit_id=unit)
    return query.all()

def get_courses(session, formation=None, unit=None):
    query = session.query(sch.Course).join(sch.Option)
    if formation:
        query = query.filter(sch.Option.formation_id==formation)
    if unit:
        query = query.filter(sch.Option.unit_id==unit)
    return query.all()

def get_course(session, key):
    query = session.query(sch.Course)
    query = query.filter_by(id=key)
    return query.one()
