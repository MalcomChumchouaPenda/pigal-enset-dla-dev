
import os
from core.utils import get_store


store = get_store('demo')

def get_courses():
    return store.read_json('md/courses-tests.json')

def get_course_types(short=True):
    if short is True:
        return store.read_markdown('md/course-types-150.md')
    return store.read_markdown('md/course-types-300.md')

def get_research_labs():
    return store.read_json('json/research.json')

def get_events():
    return store.read_json('json/events.json')


def get_intro(topic, size):
    return store.read_markdown(f'md/intro-{topic}-{size}.md')

def get_departments():
    return store.read_json('json/departments.json')

def get_formations():
    return store.read_json('json/formations.json')

def get_labs():
    return store.read_json('json/labs.json')


# LRVB - LGPR - LME - GIA - LASED - LAREGA - LAMPE

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
