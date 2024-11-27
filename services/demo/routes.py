
from core.utils import create_api
from . import queries as qry


api = create_api('demo')


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


