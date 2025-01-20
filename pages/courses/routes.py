
from flask import render_template, request
from flask_paginate import Pagination, get_page_args
from core.utils import create_ui, get_assets
from core.config import db
from services.demo import queries as qry


ui = create_ui('courses')
assets = get_assets('courses')


@ui.route('/')
def index():
    session = db.session
    return render_template('courses.html',
                           labs=qry.get_labs(session),
                           formations=qry.get_formations(session),
                           departments=qry.get_departments(session))

# def _load_formations():
#     items = qry.get_formations()
#     for item in items:
#         key = item['id'].lower()
#         text_path = f'md/formations/{key}-100.md'
#         if assets.is_file(text_path):
#             item['text'] = assets.read_markdown(text_path)
#             item['image'] = f'img/formations/{key}-original.jpg'
#     return items

# def _load_departments():
#     items = qry.get_departments()
#     for item in items:
#         key = item['id'].lower()
#         text_path = f'md/departments/{key}-50.md'
#         item['text'] = assets.read_markdown(text_path)
#         item['image'] = f'img/departments/{key}-400x200.jpg'
#     return items

# def _load_labs():
#     items = qry.get_labs()
#     for item in items:
#         key = item['id'].lower()
#         text_path = f'md/labs/{key}-50.md'
#         item['text'] = assets.read_markdown(text_path)
#         item['image'] = f'img/labs/{key}-400x200.jpg'
#     return items


@ui.route("/list", defaults={'formation':None, 'unit':None})
@ui.route("/list/all", defaults={'formation':None, 'unit':None})
@ui.route("/list/all/<unit>", defaults={'formation':None})
@ui.route("/list/<formation>", defaults={'unit':None})
@ui.route("/list/<formation>/<unit>")
def list(formation, unit):
    header = _create_list_header(formation, unit)
    courses = qry.get_courses(db.session, formation=formation, unit=unit)
    courses, pagination = _create_paginated_courses(courses)
    # courses = _add_description(courses)
    return render_template('courses-listing.html', 
                            header=header,
                            courses=courses,
                            pagination=pagination)

def _create_list_header(formation, unit):
    title = 'Formations'
    if formation is None:
        if unit is None:
            link = '...'
        else:
            link = unit.upper()
            title += f' {link}'
    else:
        formation = formation.upper()
        if unit is None:
            title += f' {formation}'
            link = formation
        else:
            unit = unit.upper()
            link = f'{unit} ({formation})'
            title += f' {link}'
    return dict(title=title, link=link)

def _create_paginated_courses(courses):
    page_args = get_page_args(page_parameter='page', 
                              per_page_parameter='per_page')
    page, per_page, offset = page_args
    page_courses = courses[offset: offset + per_page]
    page_total = len(page_courses)
    total = len(courses)
    info = f'{offset+1} à {offset + page_total} résultats sur {total}'
    pagination = Pagination(page=page, per_page=per_page, total=total, 
                            css_framework='bootstrap5', display_msg=info)
    return page_courses, pagination

# def _add_description(courses):
#     default = assets.read_markdown('md/courses/default-50.md')
#     for course in courses:
#         course['text'] = default
#     return courses
    

@ui.route('/details')
def details():
    prev_url = request.args.get('prev_url')
    prev = request.args.get('prev')
    key = request.args.get('key')
    course = qry.get_course(db.session, key)
    return render_template('courses-details.html', 
                           course=course,
                           prev_url=prev_url, 
                           prev=prev)

