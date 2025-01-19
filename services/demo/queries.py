
import os
# import pandas as pd
from core.utils import get_store


store = get_store('demo')


def get_pays():
    return store.read_json('json/pays.json')

def get_professions():
    return store.read_json('json/professions.json')


def get_events():
    return store.read_json('json/events.json')

def get_departments():
    return store.read_json('json/departments.json')

def get_formations():
    return store.read_json('json/formations.json')

def get_labs():
    return store.read_json('json/labs.json')

def get_diplomas():
    return store.read_json('json/diplomas.json')

def get_options(formation=None, unit=None):
    options = store.read_json('json/options.json')
    if formation:
        options = [o for o in options if o['formation_id']==formation]
    if unit:
        options = [o for o in options if o['unit_id']==unit]
    return options

def get_courses(formation=None, unit=None):
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

def get_course(key):
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


def get_formations_by_department(type_):
    departments = store.read_json('json/departments.json')
    fkey = type_.lower()
    items = []
    for department in departments:
        dkey = department['id'].lower()
        text_path = f'md/{fkey}-{dkey}-50.md'
        if store.is_file(text_path):
            text = store.read_markdown(text_path)
            item = department.copy()
            item['text'] = text
            item['key'] = f'{fkey}-{dkey}'
            item['image'] = f'formations/{fkey}-{dkey}-400x200.jpg'
            items.append(item)
    return items

def get_formations_by_lab():
    labs = store.read_json('json/labs.json')
    fkey = 'm2r'
    items = []
    for lab in labs:
        lkey = lab['id'].lower()
        text_path = f'md/{fkey}-{lkey}-50.md'
        if store.is_file(text_path):
            text = store.read_markdown(text_path)
            item = lab.copy()
            item['text'] = text
            item['key'] = f'{fkey}-{lkey}'
            item['image'] = f'formations/{fkey}-{lkey}-400x200.jpg'
            items.append(item)
    return items


def get_unit_by_key(key):
    fkey, ukey = key.split('-')
    if fkey == 'm2r':
        unit = get_lab_by_key(ukey)
    else:
        unit = get_department_by_key(ukey)
    unit['image'] = f'formations/{fkey}-{ukey}-400x200.jpg'
    unit['formation'] = get_formation_by_key(fkey)
    return unit

def get_formation_by_key(fkey):
    formations = store.read_json('json/formations.json')
    formations = {item['id']:item for item in formations}
    return formations[fkey.upper()]

def get_lab_by_key(lkey):
    labs = store.read_json('json/labs.json')
    labs = {item['id']:item for item in labs}
    return labs[lkey.upper()]

def get_department_by_key(dkey):
    departments = store.read_json('json/departments.json')
    departments = {item['id']:item for item in departments}
    return departments[dkey.upper()]
