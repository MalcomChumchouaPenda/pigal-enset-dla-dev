
import os
import re
import json
from datetime import datetime
from importlib import import_module

import markdown as md
from flask import render_template
from flask_security import hash_password

from .config import app, db, migrate, security
from .config import PAGES_DIR, SERVICES_DIR, PORTALS


# DATABASE METHODS

def init_db():
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()
        if not security.datastore.find_user(email="test@me.com"):
            security.datastore.create_user(email="test@me.com", password=hash_password("password"))
        db.session.commit()


# FILES I/O METHODS

def list_encoding():
    r=[]
    for i in os.listdir(os.path.split(__import__("encodings").__file__)[0]):
        name=os.path.splitext(i)[0]
        try:
            "".encode(name)
        except:
            pass
        else:
            r.append(name.replace("_","-"))
    return r

encodings = list_encoding()

def read_text(filepath, encoding='utf-8', coerce=True):
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            text = f.read()
    except UnicodeDecodeError:
        if not coerce:
            raise
        valid = None
        for enc in encodings:
            print('- test read with', enc, 'for', filepath)
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    text = f.read()
                    valid = True
            except UnicodeDecodeError:
                continue
        if not valid:
            raise RuntimeError(f'Unable to read text in {filepath}')
    return text


def read_json(filepath, encoding='utf-8', coerce=True):
    text = read_text(filepath, encoding=encoding, coerce=coerce)
    data = json.loads(text)
    return data

def read_markdown(filepath, encoding='utf-8', coerce=True):
    text = read_text(filepath, encoding=encoding, coerce=coerce)
    return md.markdown(text)


# STORE/ASSETS ACCESS METHODS

class __Folder:

    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def read_json(self, filename, encoding='utf-8', coerce=True):
        filepath = os.path.join(self.folder, filename)
        filepath = os.path.normpath(filepath)
        return read_json(filepath, 
                         encoding=encoding, 
                         coerce=coerce)

    def read_markdown(self, filename, encoding='utf-8', coerce=True):
        filepath = os.path.join(self.folder, filename)
        filepath = os.path.normpath(filepath)
        return read_markdown(filepath, 
                             encoding=encoding, 
                             coerce=coerce)
    
    def is_file(self, filename):
        return os.path.isfile(os.path.join(self.folder, filename))
    

def get_store(apiname):
    folder = os.path.join(SERVICES_DIR, apiname, 'store')
    return __Folder(folder)

def get_assets(uiname):
    folder = os.path.join(PAGES_DIR, uiname, 'assets')
    return __Folder(folder)


# DEFAULT PAGES

def default_deadline():
    now = datetime.now()
    return f'{now.year}/12/31'

def render_coming_soon(title, style, deadline=default_deadline()):
    with app.app_context():
        page = render_template(f'{style}-coming-soon.html', 
                               title=title, deadline=deadline)
    return page


# CUSTOM FILTERS

@app.template_filter('safe_md')
def convert_to_safe(md_link):
    if '/store/' in md_link:
        md_dir = SERVICES_DIR
    elif '/assets/' in md_link:
        md_dir = PAGES_DIR
    else:
        raise RuntimeError(f'Invalid Path -> {md_link}')
    if md_link.startswith('/'):
        md_link = md_link[1:]
    md_link = os.path.normpath(md_link)
    filename = os.path.join(md_dir, md_link)
    safe = app.jinja_env.filters['safe']
    return safe(read_markdown(filename))


# CONTEXT PROCESSORS

@app.context_processor
def inject_utils():
    return {'default_deadline':default_deadline, 
            'portals': PORTALS}
