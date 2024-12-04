
from flask import render_template
from flask_paginate import Pagination, get_page_args
from core.utils import create_ui, get_assets


ui = create_ui('events')
assets = get_assets('events')


@ui.route('/')
def index():
    events = assets.read_json('json/events.json')
    events, pagination = _create_paginated_events(events)
    return render_template('events.html', 
                           events=events,
                           pagination=pagination)

def _create_paginated_events(events):
    page_args = get_page_args(page_parameter='page', 
                              per_page_parameter='per_page')
    page, per_page, offset = page_args
    page_events = events[offset: offset + per_page]
    page_total = len(page_events)
    total = len(events)
    info = f'{offset+1} à {offset + page_total} résultats sur {total}'
    pagination = Pagination(page=page, per_page=per_page, total=total, 
                            css_framework='bootstrap5', display_msg=info)
    return page_events, pagination

@ui.route('/details/<id>')
def details(id):
    events = assets.read_json('json/events.json')
    events = _add_description(events)
    for event in events:
        if event['id'] == id:
            return render_template('events-details.html', event=event)


def _add_description(events):
    for item in events:
        item_id = item["id"]
        item['text'] = assets.read_markdown(f'md/{item_id}-100.md')
    return events