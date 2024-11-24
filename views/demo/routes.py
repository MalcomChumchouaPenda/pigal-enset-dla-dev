
import os
from flask import render_template, session, url_for
from core.utils import create_ui, register_entry
from core.utils import read_json, read_markdown


_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
_ASSET_DIR = os.path.join(_CUR_DIR, 'assets')
_IMG_DIR = os.path.join(_ASSET_DIR, 'img')
_JSON_DIR = os.path.join(_ASSET_DIR, 'json')
_IMG_URL = 'img/'
_JSON_URL = 'json/'


ui = create_ui('demo')
register_entry('home', 'Home', 'landing', 'demo.index')
register_entry('sections', 'Sections', 'landing')
register_entry('blank', 'Blank', 'sections', 'demo.blank')
register_entry('coming-soon', 'Under Construction', 'sections', 'demo.coming_soon')


@ui.route('/')
@ui.route('/index')
def index():
    return render_template('demo-index.html')

@ui.route('/blank')
def blank():
    return render_template('demo-blank.html')

@ui.route('/coming-soon')
def coming_soon():
    return render_template('demo-coming-soon.html', deadline='2024/12/31')

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

@ui.route('/contact')
def contact():
    return render_template('demo-contact.html')


@ui.route('/hero')
@ui.route('/hero/<kind>')
def hero(kind=None):
    if kind is None:
        return render_template('demo-hero.html')
    return render_template(f'demo-hero-{kind}.html')
