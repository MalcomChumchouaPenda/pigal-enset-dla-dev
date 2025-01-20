
from core.utils import get_store
from . import schemas as sch


store = get_store('demo')


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
