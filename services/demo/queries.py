
import os
from core.utils import get_store


store = get_store('demo')

def get_courses():
    return store.read_json('courses-tests.json')

def get_course_types(short=True):
    if short is True:
        return store.read_markdown('course-types-150.md')
    return store.read_markdown('course-types-300.md')

def get_research_labs():
    return store.read_json('research.json')

def get_events():
    return store.read_json('events.json')

def get_formations_by_department(type_):
    departments = store.read_json('departments.json')
    fkey = type_.lower()
    items = []
    for department in departments:
        dkey = department['id'].lower()
        text_path = f'formations-50/{fkey}-{dkey}.md'
        if store.is_file(text_path):
            text = store.read_markdown(text_path)
            item = department.copy()
            item['text'] = text
            item['image'] = f'formations/{fkey}-{dkey}.jpg'
            items.append(item)
    return items

def get_formations_by_lab():
    labs = store.read_json('labs.json')
    fkey = 'm2r'
    items = []
    for lab in labs:
        lkey = lab['id'].lower()
        text_path = f'formations-50/{fkey}-{lkey}.md'
        if store.is_file(text_path):
            text = store.read_markdown(text_path)
            item = lab.copy()
            item['text'] = text
            item['image'] = f'formations/{fkey}-{lkey}.jpg'
            items.append(item)
    return items