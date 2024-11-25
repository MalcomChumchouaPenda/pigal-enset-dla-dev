
import os
from flask import render_template, session, url_for
from core.utils import create_ui, add_entry
from core.utils import read_json, read_markdown


_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
_ASSET_DIR = os.path.join(_CUR_DIR, 'assets')
_IMG_DIR = os.path.join(_ASSET_DIR, 'img')
_JSON_DIR = os.path.join(_ASSET_DIR, 'json')
_IMG_URL = 'img/'
_JSON_URL = 'json/'


ui = create_ui('demo')
add_entry('landing', 1, 'home', 'Home', point='demo.index')
add_entry('landing', 2, 'pages', 'Pages')
add_entry('landing', 3, 'sections', 'Sections')
add_entry('landing', 4, 'contact', 'Contact')

add_entry('pages', 1, 'blank', 'Blank', point='demo.blank')
add_entry('pages', 2, 'coming', 'Under Construction', point='demo.coming_soon')
add_entry('pages', 3, '404', '404', url='/not-found')

add_entry('sections', 1, 'hero1', 'Hero standard', point='demo.hero')
add_entry('sections', 2, 'hero2', 'Hero large', point='demo.hero', kind='large')
add_entry('sections', 3, 'hero3', 'Hero small', point='demo.hero', kind='small')
add_entry('sections', 4, 'hero4', 'Hero carousel', point='demo.hero', kind='carousel')
add_entry('sections', 5, 'about', 'About', point='demo.about')
add_entry('sections', 6, 'services', 'Services', point='demo.services')
add_entry('sections', 7, 'speechs', 'Speechs', point='demo.speechs')


@ui.route('/')
@ui.route('/index')
def index():
    return render_template('demo-index.html')

@ui.route('/blank')
def blank():
    return render_template('demo-blank.html')

@ui.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon.html', deadline='2024/12/31')

@ui.route('/about')
def about():
    items = read_json(os.path.join(_JSON_DIR, 'about.json'))
    for item in items.values():
        md_path = os.path.join(_ASSET_DIR, item['text'])
        md = read_markdown(md_path)
        item['text'] = md
        # print(md)
    return render_template('demo-about.html', items=items)

@ui.route('/services')
def services():
    data1 = read_json(os.path.join(_JSON_DIR, 'services.json'))
    data2 = data1[:5]
    data3 = data1[:4]
    data4 = data1[:3]
    return render_template('demo-services.html', 
                           data1=data1, data2=data2, 
                           data3=data3, data4=data4)

@ui.route('/speechs')
def speechs():
    items = read_json(os.path.join(_JSON_DIR, 'speechs.json'))
    md_path = os.path.join(_ASSET_DIR, items['main']['text'])
    md = read_markdown(md_path)
    items['main']['text'] = md
    return render_template('demo-speechs.html', items=items)
    
    

@ui.route('/portfolio')
def portfolio():
    return render_template('demo-portfolio.html')

@ui.route('/team')
def team():
    return render_template('demo-team.html')

@ui.route('/blog')
def blog():
    return render_template('demo-blog.html')

@ui.route('/projects')
def projects():
    return render_template('demo-projects.html')

@ui.route('/hero')
@ui.route('/hero/<kind>')
def hero(kind=None):
    if kind is None:
        return render_template('demo-hero.html')
    return render_template(f'demo-hero-{kind}.html')
