
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
    categories = init_categories(session)
    _ = init_events(session, categories)
    _ = init_pays(session)
    _ = init_professions(session)
    _ = init_formations(session)
    _ = init_departments(session)
    _ = init_labs(session)
    _ = init_levels(session)
    _ = init_diplomas(session)
    _ = init_options(session)
    _ = init_courses(session)

def init_categories(session):
    names = ['Formation', 'Organisation', 'Recherche']
    result = {}
    for name in names:
        id_ = name[:3].upper()
        category = sch.Category(id=id_, name=name)
        result[name] = category
        session.merge(category)
    session.commit()
    return result

def init_events(session, categories):
    records = store.read_json('json/events.json')
    result = []
    for record in records:
        record['date'] = dt.strptime(record['date'], TIME_EXP)
        record['category'] = categories[record['category']]
        obj = sch.Event(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_pays(session):
    records = store.read_json('json/pays.json')
    result = []
    for record in records:
        obj = sch.Pays(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_professions(session):
    records = store.read_json('json/professions.json')
    result = []
    for record in records:
        obj = sch.Profession(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_formations(session):
    records = store.read_json('json/formations.json')
    result = []
    for record in records:
        obj = sch.Formation(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_departments(session):
    records = store.read_json('json/departments.json')
    result = []
    for record in records:
        obj = sch.Department(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_labs(session):
    records = store.read_json('json/labs.json')
    result = []
    for record in records:
        obj = sch.Lab(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_levels(session):
    records = store.read_json('json/levels.json')
    result = []
    for record in records:
        obj = sch.Level(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_diplomas(session):
    records = store.read_json('json/diplomas.json')
    result = []
    for record in records:
        obj = sch.Diploma(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_options(session):
    records = store.read_json('json/options.json')
    result = []
    for record in records:
        obj = sch.Option(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result

def init_courses(session):
    records = store.read_json('json/courses.json')
    result = []
    for record in records:
        obj = sch.Course(**record)
        session.merge(obj)
        result.append(obj)
    session.commit()
    return result


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

