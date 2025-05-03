
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

ui.register_entry('home_menu', 'home_demo1', _l('Pages'))
ui.register_entry('home_menu', 'home_demo2', _l('Sections'))
ui.register_entry('home_menu', 'home_demo3', _l('Dashboards'), rank=2)


# PAGES

ui.register_entry('home_demo1', 'home_demo1_1', _l('Page vide'), endpoint='demo.blank', rank=0)
ui.register_entry('home_demo1', 'home_demo1_2', _l('Page avec menu'), endpoint='demo.menu', rank=1)
ui.register_entry('home_demo1', 'home_demo1_3', _l('Page de message'), url='/demo/message', rank=4)
ui.register_entry('home_demo1', 'home_demo1_4', _l('Page Attente'), endpoint='demo.coming_soon', rank=5)


@ui.route('/')
@ui.route('/blank')
def blank():
    return render_template('demo-blank.jinja')

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


# PAGES (POUR UN MENU SPECIAL)

ui.register_menu('demo_menu')
ui.register_entry('demo_menu', 'demo0', _l('Accueil'), endpoint='home.index', rank=0)
ui.register_entry('demo_menu', 'demo1', _l('Page 1'), url='#', rank=1)
ui.register_entry('demo_menu', 'demo2', _l('Page 2'), url='#', rank=2)
ui.register_entry('demo_menu', 'demo3', _l('Menus'), rank=3)
ui.register_entry('demo3', 'demo3_1', _l('Menu (ordonnee)'))
ui.register_entry('demo3', 'demo3_2', _l('Menu (reordonne)'))
ui.register_entry('demo3_1', 'demo3_1_1', _l('Page 1'), url='#')
ui.register_entry('demo3_1', 'demo3_1_2', _l('Page 2'), url='#')
ui.register_entry('demo3_2', 'demo3_2_1', _l('Page 1'), url='#', rank=1)
ui.register_entry('demo3_2', 'demo3_2_2', _l('Page 2'), url='#', rank=0)

@ui.route('/menu')
def menu():
    return render_template('demo-menu.jinja')


# PAGES (DIFFERENTS HEROS)

ui.register_entry('home_demo1', 'home_demo1_5', _l('Page avec hero'), rank=2)
ui.register_entry('home_demo1_5', 'home_demo1_5_1', _l('Hero large'), url='/demo/hero/lg')
ui.register_entry('home_demo1_5', 'home_demo1_5_2', _l('Hero moyen'), url='/demo/hero/md')
ui.register_entry('home_demo1_5', 'home_demo1_5_3', _l('Hero reduit'), url='/demo/hero/sm')
ui.register_entry('home_demo1_5', 'home_demo1_5_4', _l('Hero carousel'), url='/demo/hero/carousel')

@ui.route('/hero/<size>')
def hero(size):
    return render_template(f'demo-hero-{size}.jinja')

@ui.route('/hero/carousel')
def hero_carousel():
    items = [{'title': _('This is demo %(i)s', i=i),
              'image': f'img/slides-{i}.jpg'}
                for i in range(1, 4)]
    return render_template('demo-hero-carousel.jinja', items=items)


# PAGES (DIFFERENTS FOOTERS)

ui.register_entry('home_demo1', 'home_demo1_6', _l('Page avec footer'), rank=3)
ui.register_entry('home_demo1_6', 'home_demo1_6_1', _l('Footer large'), url='/demo/footer/lg', rank=0)
ui.register_entry('home_demo1_6', 'home_demo1_6_2', _l('Footer moyen'), url='/demo/footer/md', rank=1)
ui.register_entry('home_demo1_6', 'home_demo1_6_3', _l('Footer reduit'), url='/demo/footer/sm', rank=2)
ui.register_entry('home_demo1_6', 'home_demo1_6_4', _l('Footer avec auteurs'), url='/demo/footer/authors', rank=3)

@ui.route('/footer/<size>')
def footer(size):
    return render_template(f'demo-footer-{size}.jinja')

@ui.route('/footer/authors')
def authors():
    return render_template('demo-footer-authors.jinja')


# SECTIONS DE PAGE

ui.register_entry('home_demo2', 'home_demo2_1', _l('Services'), endpoint='demo.services', rank=0)
ui.register_entry('home_demo2', 'home_demo2_2', _l('About'), endpoint='demo.about', rank=1)
ui.register_entry('home_demo2', 'home_demo2_3', _l('Recherche'), endpoint='demo.search', rank=2)
ui.register_entry('home_demo2', 'home_demo2_4', _l('Evenements'), endpoint='demo.events', rank=3)
ui.register_entry('home_demo2', 'home_demo2_5', _l('Attente'), endpoint='demo.coming_soon_sections', rank=4)


@ui.route('/sections/coming-soon')
def coming_soon_sections():
    return render_template('demo-coming-soon-sections.jinja')

@ui.route('/services')
def services():
    locale = get_locale()
    itemspath = os.path.join(static_dir, f'json/services_{locale}.json')
    return render_template('demo-services.jinja', items=read_json(itemspath))

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
    return render_template('demo-about.jinja', 
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
    return render_template('demo-search.jinja',
                           pagination=pagination,
                           keywords=keywords,
                           results=items)


@ui.route('/events')
def events():
    items = [{'title':_("Titre de l'evenement %(i)s", i=i),
              'image': url_for('demo.static', filename=f'img/event-{i}.jpg'),
              'category': _('Paire') if i%2 == 0 else _('Impaire'),
              'date': '10/02/2021'}
                for i in range(1, 7)]
        
    page = int(request.args.get('page', 1))
    items, pagination = paginate_items(items, page, per_page=12)
    return render_template('demo-events.jinja',
                           pagination=pagination,
                           items=items)


# DASHBOARDS

ui.register_entry('home_demo3', 'home_demo3_1', _l('Dashboard (avec composants)'), endpoint='demo.dashboard', rank=0)
ui.register_entry('home_demo3', 'home_demo3_2', _l('Dashboard (protege)'), endpoint='demo.protected', rank=1)
ui.register_entry('home_demo3', 'home_demo3_3', _l('Dashboard (etudiants)'), endpoint='demo.student', rank=2)

ui.register_domain('g1',_l('Form Components'))
ui.register_dashboard('g1', 'd1', _l('Form editors'), endpoint='demo.form_editors')
ui.register_dashboard('g1', 'd2', _l('Form elements'), endpoint='demo.form_elements')
ui.register_dashboard('g1', 'd3', _l('Form layouts'), endpoint='demo.form_layouts')
ui.register_dashboard('g1', 'd4', _l('Form validation'), endpoint='demo.form_validation')

ui.register_domain('g2', _l('Data Components'))
ui.register_dashboard('g2', 'd4', _l('General tables'), endpoint='demo.tables')
ui.register_dashboard('g2', 'd5', _l('Data tables'), endpoint='demo.datatables')
ui.register_dashboard('g2', 'd6', _l('Data charts'), endpoint='demo.charts')


@ui.route('/dashboard')
def dashboard():
    welcome = _("Cette espace presente des composants demo")
    return render_template('dashboard/home.jinja',
                           domain_ids=['g1', 'g2'],  
                           welcome=welcome)


@ui.route('/charts')
def charts():
    return render_template('demo-charts.jinja')

@ui.route('/tables')
def tables():
    persons = [
        {'name':'Brandon Jacob', 'positions':'Designer', 'age':28, 'start_date':'2016-05-25'},
        {'name':'Bridie Kessler', 'positions':'Developper', 'age':35, 'start_date':'2014-12-05'},
        {'name':'Ashleigh Langosh', 'positions':'Finance', 'age':45, 'start_date':'2011-08-12'},
        {'name':'Angus Grady', 'positions':'HR', 'age':34, 'start_date':'2012-06-11'},
        {'name':'Raheem Lehner', 'positions':'Designer', 'age':47, 'start_date':'2011-04-19'},
    ]
    return render_template('demo-tables.jinja', persons=persons)

@ui.route('/datatables')
def datatables():
    addrspath = os.path.join(static_dir, 'json/addresses.json')
    return render_template('demo-datatables.jinja', addresses=read_json(addrspath))


@ui.route('/form-editors')
def form_editors():
    return render_template('demo-form-editors.jinja')


@ui.route('/form-elements')
def form_elements():
    return render_template('demo-form-elements.jinja')


@ui.route('/form-layouts')
def form_layouts():
    return render_template('demo-form-layouts.jinja')


@ui.route('/form-validation')
def form_validation():
    return render_template('demo-form-validation.jinja')


# @ui.route('/unprotected')
# def unprotected():
#     message="Welcome in a free space"
#     return render_template('home-space.jinja', message=message)

@ui.route('/protected')
@ui.login_required
def protected():
    message = _("Welcome in a protected space")
    return render_template('dashboard/home.jinja',welcome=message)

@ui.route('/student')
@ui.roles_accepted('student')
def student():
    message = _("Welcome in student space")
    return render_template('dashboard/home.jinja',welcome=message)

