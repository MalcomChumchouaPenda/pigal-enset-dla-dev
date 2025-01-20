
from datetime import datetime as dt
from core.config import db
from core.utils import create_api, get_store
from . import queries as qry
from . import schemas as sch


api = create_api('demo', local_db=True)
store = get_store('demo')
TIME_EXP = r'%d/%m/%Y'


@api.before_app_first_request
def init_db():
    session = db.session
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


@api.route('/')
def root():
    return {'info':'Demo Api'}

@api.route("/formations")
def get_formations():
    return qry.get_formations()

@api.route("/diplomas")
def get_diplomas():
    return qry.get_diplomas()

@api.route("/departments")
def get_departments():
    return qry.get_departments()

@api.route("/labs")
def get_labs():
    return qry.get_labs()

@api.route("/options", defaults={'formation':None, 'unit':None})
@api.route("/options/~/<unit>", defaults={'formation':None})
@api.route("/options/<formation>", defaults={'unit':None})
@api.route("/options/<formation>/<unit>")
def get_options(formation, unit):
    return qry.get_options(formation=formation, unit=unit)

@api.route("/courses", defaults={'formation':None, 'unit':None})
@api.route("/courses/~/<unit>", defaults={'formation':None})
@api.route("/courses/<formation>", defaults={'unit':None})
@api.route("/courses/<formation>/<unit>")
def get_courses(formation, unit):
    return qry.get_courses(formation=formation, unit=unit)

