
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
        event = sch.Event(**record)
        session.merge(event)
        result.append(event)
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

