
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


@ui.route("/list", defaults={'formation':None, 'unit':None})
@ui.route("/list/all", defaults={'formation':None, 'unit':None})
@ui.route("/list/all/<unit>", defaults={'formation':None})
@ui.route("/list/<formation>", defaults={'unit':None})
@ui.route("/list/<formation>/<unit>")
def list(formation, unit):
    diplomas = qry.get_diplomas()
    courses = qry.get_courses(formation=formation, unit=unit)
    for item in diplomas:
        item['courses'] = [c for c in courses 
                           if c['diploma_id']==item['id']]
    header = _create_list_header(formation, unit)
    return render_template('courses-list.html', 
                           header=header,
                           unit=unit,
                           diplomas=diplomas,
                           formation=formation)

def _create_list_header(formation, unit):
    if formation is None and unit is None:
        title = 'Liste complete des offres de formation'
        image = 'img/hero-bg.jpg'
        link = '...'
    elif formation is not None and unit is None:
        title = f'Liste des formations de {formation}'
        link = f'{formation.upper()}'
        image = f'img/formations/{formation.lower()}-400x200.jpg'      
    elif formation is None and unit is not None:
        title = f'Liste des formations de {unit}'
        link = f'{unit.upper()}'
        if formation == 'M2R':
            image = f'img/labs/{unit.lower()}-400x200.jpg'
        else:
            image = f'img/departments/{unit.lower()}-400x200.jpg'
    else:
        title = f'Liste des formations {formation} de {unit}'
        link = f'{unit.upper()} ({formation.upper()})'
        if formation == 'M2R':
            image = f'img/labs/{unit.lower()}-400x200.jpg'
        else:
            image = f'img/departments/{unit.lower()}-400x200.jpg'
    return dict(title=title, link=link, image=image)



@ui.route('/<key>')
def details(key):
    unit = qry.get_unit_by_key(key)
    return render_template('courses-details.html',
                           unit=unit)