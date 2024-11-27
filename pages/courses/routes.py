
from flask import render_template
from core.utils import create_ui, get_assets
from services.demo import queries as qry


ui = create_ui('courses')
assets = get_assets('courses')

@ui.route('/')
def index():
    return render_template('courses.html', 
                           labs=_load_labs(),
                           formations=_load_formations(),
                           departments=_load_departments())

def _load_formations():
    items = qry.get_formations()
    for item in items:
        key = item['id'].lower()
        text_path = f'md/formations/{key}-100.md'
        if assets.is_file(text_path):
            item['text'] = assets.read_markdown(text_path)
            item['image'] = f'img/formations/{key}-original.jpg'
    return items


def _load_departments():
    items = qry.get_departments()
    for item in items:
        key = item['id'].lower()
        text_path = f'md/departments/{key}-50.md'
        item['text'] = assets.read_markdown(text_path)
        item['image'] = f'img/departments/{key}-400x200.jpg'
    return items

def _load_labs():
    items = qry.get_labs()
    for item in items:
        key = item['id'].lower()
        text_path = f'md/labs/{key}-50.md'
        item['text'] = assets.read_markdown(text_path)
        item['image'] = f'img/labs/{key}-400x200.jpg'
    return items


@ui.route('/<key>')
def details(key):
    unit = qry.get_unit_by_key(key)
    return render_template('courses-details.html',
                           unit=unit)