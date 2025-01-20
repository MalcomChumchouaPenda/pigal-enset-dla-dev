
import os
# import pandas as pd
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
        query = query.filter_by(sch.Option.unit_id==unit)
    return query.all()
    return [course for course, _ in query.all()]
    courses = store.read_json('json/courses.json')
    diplomas = store.read_json('json/diplomas.json')
    diplomas = {d['id']:d for d in diplomas}
    levels = store.read_json('json/levels.json')
    levels = {l['id']:l for l in levels}
    options = get_options(formation=formation, unit=unit)
    options = {o['id']:o for o in options}
    filters = list(options.keys())
    results = []
    for course in courses:
        option_id = course['option_id']
        if  option_id in filters:
            option = options[option_id]
            diploma_id = course['diploma_id']
            diploma = diplomas[diploma_id]
            level_id = course['level_id']
            level = levels[level_id]
            course['level_name'] = level['nom']
            course['diploma_name'] = diploma['nom']
            course['formation_id'] = option['formation_id']
            course.update(options[course['option_id']])
            course['id'] = f"{option_id}-{level_id}"
            results.append(course)
    return results

def get_course(session, key):
    query = session.query(sch.Course)
    query = query.filter_by(id=key)
    return query.one()
    diplomas = store.read_json('json/diplomas.json')
    diplomas = {d['id']:d for d in diplomas}
    levels = store.read_json('json/levels.json')
    levels = {l['id']:l for l in levels}
    options = store.read_json('json/options.json')
    options = {o['id']:o for o in options}
    courses = store.read_json('json/courses.json')
    for course in courses:
        option_id = course['option_id']
        level_id = course['level_id']
        course_id = f"{option_id}-{level_id}"
        if key == course_id:
            option = options[option_id]
            diploma_id = course['diploma_id']
            diploma = diplomas[diploma_id]
            level = levels[level_id]
            course['level_name'] = level['nom']
            course['diploma_name'] = diploma['nom']
            course['formation_id'] = option['formation_id']
            course.update(options[course['option_id']])
            course['id'] = course_id
            return course
