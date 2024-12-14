
import os
from uuid import uuid4
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase


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

default_db = os.path.join(STORE_DIR, 'main.db')
migrations_dir = os.path.join(STORE_DIR, 'migrations')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{default_db}"
app.config['SQLALCHEMY_BINDS'] = {}
db = SQLAlchemy(model_class=DeclarativeBase)
migrate = Migrate(directory=migrations_dir)


# LOGIN CONFIGURATION

PORTALS = [        
    {'nom':'Admissions', 'id':'candidate'},
    {'nom':'Etudiants', 'id':'student'},
    {'nom':'Enseignants', 'id':'teacher'},
    {'nom':'Administration', 'id':'admin'},
]
