
import os
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l
from flask import render_template, request, url_for, redirect
from core.utils import (
    UiBlueprint, 
    read_json, 
    read_markdown, 
    paginate_items, 
    default_deadline,
    get_locale
)


ui = UiBlueprint(__name__)
static_dir = os.path.join(os.path.dirname(__file__), 'static')


@ui.route('/')
@ui.route('/blank')
def blank():
    return render_template('demo-landing-blank.jinja')

@ui.route('/message')
def message():
    return render_template('landing/message.jinja',
                           title=_("Avertissement"),
                           message=_("Ceci est un message test"),
                           actions = [{'text':_("Revenir a l'accueil"), 'url':'/'}])

@ui.route('/coming-soon')
def coming_soon():
    return render_template('landing/coming-soon.jinja',
                           deadline=default_deadline(), 
                           title='demo')



# PAGES (DIFFERENTS HEROS)

@ui.route('/hero/<size>')
def hero(size):
    return render_template(f'demo-landing-hero-{size}.jinja')

@ui.route('/hero/carousel')
def hero_carousel():
    items = [{'title': _('This is demo %(i)s', i=i),
              'image': f'img/slides-{i}.jpg'}
                for i in range(1, 4)]
    return render_template('demo-landing-hero-carousel.jinja', items=items)


# PAGES (DIFFERENTS FOOTERS)

@ui.route('/footer/<size>')
def footer(size):
    return render_template(f'demo-landing-footer-{size}.jinja')

@ui.route('/footer/authors')
def authors():
    return render_template('demo-landing-footer-authors.jinja')


# SECTIONS DE PAGE

@ui.route('/sections/coming-soon')
def coming_soon_sections():
    return render_template('demo-landing-coming-soon.jinja')

@ui.route('/services')
def services():
    locale = get_locale()
    itemspath = os.path.join(static_dir, f'json/services_{locale}.json')
    return render_template('demo-landing-services.jinja', items=read_json(itemspath))

@ui.route('/about')
def about():
    items = [
        {"icon":"bi bi-emoji-smile", "text":_("<strong>Enseignants</strong> formees par an"), "value": 250},
        {"icon":"bi bi-journal-richtext", "text":_("<strong>Ingenieurs</strong> formees par an"), "value": 540},
        {"icon":"bi bi-headset", "text":_("<strong>Programmes</strong> disponibles"), "value": 1500}
    ]   
    speechpath = os.path.join(static_dir, 'md/speech.md')
    leftaboutpath = os.path.join(static_dir, 'md/about-left.md')
    rightaboutpath = os.path.join(static_dir, 'md/about-right.md')
    return render_template('demo-landing-about.jinja', 
                           stats=items,
                           speech=read_markdown(speechpath), 
                           left_about=read_markdown(leftaboutpath), 
                           right_about=read_markdown(rightaboutpath))


@ui.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        return redirect(url_for('demo.search', keywords=keywords))

    items = [{'id':f'Item {i}', 
              'text':_("Description de l'item %(i)s pour test", i=i)}
                for i in range(0, 100)]
    keywords = request.args.get('keywords')
    if keywords is not None:
        items = [item for item in items if keywords in item['text']]
        
    page = int(request.args.get('page', 1))
    items, pagination = paginate_items(items, page, per_page=10)
    return render_template('demo-landing-search.jinja',
                           pagination=pagination,
                           keywords=keywords,
                           results=items)


@ui.route('/events')
def events():
    items = [{'title':_("Titre de l'evenement %(i)s", i=i),
              'image': url_for('demo_landing.static', filename=f'img/event-{i}.jpg'),
              'category': _('Paire') if i%2 == 0 else _('Impaire'),
              'date': '10/02/2021'}
                for i in range(1, 7)]
        
    page = int(request.args.get('page', 1))
    items, pagination = paginate_items(items, page, per_page=12)
    return render_template('demo-landing-events.jinja',
                           pagination=pagination,
                           items=items)

