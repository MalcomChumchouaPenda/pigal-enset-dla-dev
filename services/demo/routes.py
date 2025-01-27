
from flask import Blueprint
from core.config import app, db
from . import queries as qry
from . import builders as build


# create initial data
with app.app_context():
    session = db.session
    build.init_categories(session)
    build.init_events(session)
    build.init_pays(session)
    build.init_professions(session)
    build.init_formations(session)
    build.init_departments(session)
    build.init_labs(session)
    build.init_levels(session)
    build.init_diplomas(session)
    build.init_options(session)
    build.init_courses(session)


bp = Blueprint('demo', __name__,
                url_prefix=f'/demo',
                template_folder=None,
                static_folder='store')

@bp.route('/')
def root():
    return {'info':'Demo Api'}

@bp.route("/formations")
def get_formations():
    return qry.get_formations()

@bp.route("/diplomas")
def get_diplomas():
    return qry.get_diplomas()

@bp.route("/departments")
def get_departments():
    return qry.get_departments()

@bp.route("/labs")
def get_labs():
    return qry.get_labs()

@bp.route("/options", defaults={'formation':None, 'unit':None})
@bp.route("/options/~/<unit>", defaults={'formation':None})
@bp.route("/options/<formation>", defaults={'unit':None})
@bp.route("/options/<formation>/<unit>")
def get_options(formation, unit):
    return qry.get_options(formation=formation, unit=unit)

@bp.route("/courses", defaults={'formation':None, 'unit':None})
@bp.route("/courses/~/<unit>", defaults={'formation':None})
@bp.route("/courses/<formation>", defaults={'unit':None})
@bp.route("/courses/<formation>/<unit>")
def get_courses(formation, unit):
    return qry.get_courses(formation=formation, unit=unit)

