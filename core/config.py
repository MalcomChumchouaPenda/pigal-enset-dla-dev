
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
VIEWS_DIR = os.path.join(_APP_DIR, 'views')
DATA_DIR = os.path.join(_CUR_DIR, 'data')


# BASIC CONFIGURATION

app = Flask('core.config',
            template_folder='themes',
            static_folder='themes/assets',
            static_url_path='/themes/assets')
app.config['SECRET_KEY'] = uuid4().hex


# DATABASE CONFIGURATION

default_db = os.path.join(DATA_DIR, 'main.db')
migrations_dir = os.path.join(DATA_DIR, 'migrations')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{default_db}"
app.config['SQLALCHEMY_BINDS'] = {}
db = SQLAlchemy(model_class=DeclarativeBase)
migrate = Migrate(directory=migrations_dir)


# BASIC ENTRIES

LANDING_ENTRY = dict(uid='landing', children=[])
DASHBOARD_ENTRY = dict(uid='dashboard', children=[])
ENTRIES = dict(landing=LANDING_ENTRY, dashboard=DASHBOARD_ENTRY)

