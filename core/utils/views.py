
import re
from datetime import datetime
from flask import session, url_for
from flask_paginate import Pagination


def get_locale():
    lang = session.get('lang', 'fr')
    return lang

def default_deadline():
    now = datetime.now()
    return f'{now.year}/12/31'

def paginate_items(items, page, per_page=10):
    offset = (page - 1) * per_page
    page_items = items[offset: offset + per_page]
    page_total = len(page_items)
    total = len(items)
    info = f'{offset+1} à {offset + page_total} résultats sur {total}'
    options = dict(page=page, per_page=per_page, total=total,
                   css_framework='bootstrap5', display_msg=info)
    return page_items, Pagination(**options)

def url_for_entry(entry, default='#'):
    if 'point' in entry:
        kwargs = entry.get('kwargs', {})
        return url_for(entry['point'], **kwargs)
    return entry.get('url', default)


