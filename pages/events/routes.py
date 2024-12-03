
from flask import render_template
from flask_paginate import Pagination, get_page_args
from core.utils import create_ui


ui = create_ui('events')

@ui.route('/')
def index():
    news = _load_news()
    news, pagination = _create_paginated_news(news)
    return render_template('events.html', news=news,
                            pagination=pagination)

def _load_news():
    items = []
    for i in range(6):
        item = dict(
            image=f'img/news-{i+1}.jpg',
            title=f'Titre {i+1} Dolorum optio tempore voluptas dignissimos',
            category=f'Category {i+1}',
            date=f'{i}/10/2024'
        )
        items.append(item)
    return items

def _create_paginated_news(news):
    page_args = get_page_args(page_parameter='page', 
                              per_page_parameter='per_page')
    page, per_page, offset = page_args
    page_news = news[offset: offset + per_page]
    print('\t', page_args, len(page_news))
    page_total = len(page_news)
    total = len(news)
    info = f'{offset+1} à {offset + page_total} résultats sur {total}'
    pagination = Pagination(page=page, per_page=per_page, total=total, 
                            css_framework='bootstrap5', display_msg=info)
    return page_news, pagination