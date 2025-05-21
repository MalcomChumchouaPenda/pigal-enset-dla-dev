import os
import re
import json
from importlib import import_module

from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_principal import Principal
from flask_babel import Babel
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restx import Api

from core.utils import (
    get_locale,
    default_deadline,
    url_for_entry,
    ExtendedSQLAlchemy,
    PAGE_NAME_PATTERN,
    SERVICE_NAME_PATTERN,
    ROOT_DIR,
    THEMES_DIR,
    CORE_MANIFEST_PATH,
    PAGES_DIR,
    SERVICES_DIR,
)

from core.info.tasks import (
    get_contact,
    get_links
)


#-------------------------------------
# OBJETS DE CONFIGURATION
#-------------------------------------

# database objects
db = ExtendedSQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

# security objects
login_manager = LoginManager()
principal = Principal()

# internationalization objects
babel = Babel()

# api objects
api_bp = Blueprint('api', __name__)
api = Api(api_bp, 
          version='1.0', 
          title='Pigal API',
          description='A Pigal API for demo',
          doc='/doc/')


#-------------------------------------
# CLASSES DE CONFIGURATION
#-------------------------------------

class Config:

    # Configurations Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # À changer en prod
    SESSION_TYPE = 'filesystem'  # Pour stocker les sessions

    # configuration babel
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'  # Langue par défaut
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(ROOT_DIR, 'translations')


class ProdConfig(Config):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {}


class DevConfig(Config):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {}

    # activer le debogage
    DEBUG = True


class TestConfig(Config):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {}

    # Désactiver CSRF pour les tests API
    TESTING = True
    WTF_CSRF_ENABLED = False 

configs = {
    'development':DevConfig,
    'production':ProdConfig,
    'testing':TestConfig
}


#-------------------------------------
# METHODES DE CONFIGURATION
#-------------------------------------

def create_app():
    env_name = os.getenv('FLASK_ENV')
    app = Flask(__name__, 
                static_folder=THEMES_DIR, 
                template_folder=THEMES_DIR)
    
    config = prepare_db_config(env_name)
    app.config.from_object(config)
    with open(CORE_MANIFEST_PATH) as f:
        manifest = json.load(f)

    init_security(app)
    init_localization(app)
    init_globals(app)
    init_filters(app)

    app.ui_entries = []
    app.entries = {}
    app.menus = {}
    app.domains = {}
    app.register_blueprint(api_bp, url_prefix='/api')

    init_dbs(app, env_name)
    register_service(app, env_name, 'core.auth', '/auth')
    register_service(app, env_name, 'core.info', '/info')
    register_page(app, 'core.home', '/home')
    register_services(app, env_name)
    register_pages(app)
    build_menus(app)
    build_domains(app)
    return app


def prepare_db_config(env_name):
    config = configs[env_name]
    config.SQLALCHEMY_DATABASE_URI = db.get_default_uri(env_name)
    config.SQLALCHEMY_BINDS = db.get_binds(env_name)
    return config

def init_security(app):
    login_manager.init_app(app)
    principal.init_app(app)

def init_localization(app):
    babel.init_app(app, locale_selector=get_locale)
    app.jinja_env.globals.update(get_locale=get_locale)

def init_globals(app):
    app.jinja_env.globals.update(dict(
        default_deadline=default_deadline,
        url_for_entry=url_for_entry,
        get_contact=get_contact,
        get_links=get_links
    ))

def init_filters(app):
    app.jinja_env.filters.update()

def init_dbs(app, env_name):
    app.logger.info(f"creating db for: {list(app.config['SQLALCHEMY_BINDS'])}")
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    with app.app_context():
        if env_name in ['development', 'testing']:
            db.drop_all()
            app.logger.info('drop all table')
        db.create_all()
        app.logger.info('create all table')


def register_pages(app):
    app.logger.debug('looking for pages...')
    if os.path.isdir(PAGES_DIR):
        for name in os.listdir(PAGES_DIR):
            if name.startswith('_'):
                continue
            nameparts = re.findall(PAGE_NAME_PATTERN, name)
            if len(nameparts) != 1:
                app.logger.info(f'Ignore folder: {name}')
                continue
            rootname = nameparts[0].replace('_', '-')
            url_prefix = f'/{rootname}'
            ui_root = f'plugins.pages.{name}'
            register_page(app, ui_root, url_prefix)
            
def register_page(app, ui_root, url_prefix):
    try:
        routes = import_module(f'{ui_root}.routes')
        menus = import_module(f'{ui_root}.menus')
        app.register_blueprint(routes.ui, url_prefix=url_prefix)
        app.ui_entries = menus.navbar.entries
        for domain_id, domain in routes.ui.domains.items():
            if domain_id in app.domains:
                app.domains[domain_id]['dashboards'].extend(domain['dashboards'])
            else:
                app.domains[domain_id] = domain
        app.logger.info(f'Register page: {ui_root} => {url_prefix}')
        return True
    except (ModuleNotFoundError, AttributeError) as e:
        app.logger.warning(e)


def build_menus(app):
    menus = app.menus
    entries = app.entries
    for entry in app.ui_entries:
        if entry['id'] in entries:
            app.logger.warning(f'duplicated entry for {entry}')
            continue
        entries[entry['id']] = entry

    f = lambda x: (x['rank'], x['text'])
    for entry in sorted(app.ui_entries, key=f):
        if entry['parentid'] is None:
            menus[entry['id']] = entry
        else:
            parentid = entry['parentid']
            parentmenu = entries[parentid]
            parentmenu['children'].append(entry)
            if parentid not in menus:
                menus[parentid] = parentmenu
    app.jinja_env.globals.update(menus=menus)  


def build_domains(app):
    f = lambda x: (x['rank'], x['text'])
    domains = list(sorted(app.domains.values(), key=f))
    app.jinja_env.globals.update(domains=domains)  


def register_services(app, env_name):
    app.logger.debug('looking for services...')
    if os.path.isdir(SERVICES_DIR):
        for name in os.listdir(SERVICES_DIR):
            if name.startswith('_'):
                continue
            nameparts = re.findall(SERVICE_NAME_PATTERN, name)
            if len(nameparts) != 1:
                app.logger.warning('Ignore folder: '+ name)
                continue
            rootname, version = nameparts[0]
            rootname = rootname.replace('_', '-')
            version = version.replace('_', '.')
            url_prefix = f'/{rootname}/{version}'
            service_root = f'plugins.services.{name}'
            register_service(app, env_name, service_root, url_prefix)

def register_service(app, env_name, service_root, url_prefix):
    try:
        routes = import_module(f'{service_root}.routes')
        api.add_namespace(routes.ns, path=url_prefix)
        app.logger.info(f'Register service: {service_root} => {url_prefix}')
        if env_name in ['development', 'production']:
            with app.app_context():
                defaults = import_module(f'{service_root}.defaults')
                defaults.init_data()
                app.logger.info(f'Init data: {service_root}')
        return True
    except (ModuleNotFoundError, AttributeError) as e:
        app.logger.warning(e)


