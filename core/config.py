
import os
from uuid import uuid4
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# CONFIGURATION PATHS

_CUR_DIR = os.path.dirname(os.path.abspath(__file__))
_APP_DIR = os.path.dirname(_CUR_DIR)
SERVICES_DIR = os.path.join(_APP_DIR, 'services')
PAGES_DIR = os.path.join(_APP_DIR, 'pages')
STORE_DIR = os.path.join(_CUR_DIR, 'store')


# BASIC CONFIGURATION

app = Flask('core.config',
            template_folder='theme/templates',
            static_folder='theme/static',
            static_url_path='/theme/static')
app.config['SECRET_KEY'] = uuid4().hex


# DATABASE CONFIGURATION
db_binds = {}
for key in os.listdir(SERVICES_DIR):
    service_dir = os.path.join(SERVICES_DIR, key)
    if not key.startswith('_') and os.path.isdir(service_dir):
        db_path = os.path.join(STORE_DIR, f'{key}.db')
        db_binds[key] = f"sqlite:///{db_path}"
default_db_path = os.path.join(STORE_DIR, '_main.db')
migrations_dir = os.path.join(STORE_DIR, 'migrations')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{default_db_path}"
app.config['SQLALCHEMY_BINDS'] = db_binds
db = SQLAlchemy(app)
migrate = Migrate(directory=migrations_dir)


# LOGIN CONFIGURATION

PORTALS = [        
    {'nom':'Admissions', 'id':'candidate'},
    {'nom':'Etudiants', 'id':'student'},
    {'nom':'Enseignants', 'id':'teacher'},
    {'nom':'Administration', 'id':'admin'},
]
