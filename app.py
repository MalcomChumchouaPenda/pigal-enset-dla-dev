
from flask import render_template
from core.config import app, ENTRIES
from core.utils import register_api, register_ui
from core.utils import init_db
from core.utils import default_deadline
from pages.home.constants import CONTACT, LINKS, PORTALS
from pages.home.constants import LANDING_MENU, LOGIN_MENU


register_api()
register_ui()
init_db()


@app.route('/temp/<module>/<page>')
def temp(module, page):
    return f'no page "{page}" in module "{module}"'

@app.errorhandler(404)
def not_found(e):
    message = "La page que vous recherchez n'existe plus"
    actions = [{"text":"Retour a l'accueil", "point":"home.index"}]
    return render_template('base-error.html',
                           number=404,
                           message=message,
                           actions=actions)

@app.route('/login')
def login():
    return render_template('base-login.html',
                           portals=PORTALS,
                           default_portal=None)


@app.context_processor
def inject_entries():
    return {key:entry['children'] for key, entry in ENTRIES.items()}

@app.context_processor
def inject_defaults():
    return {'default_deadline':default_deadline, 
            'contact':CONTACT,
            'links':LINKS}

@app.context_processor
def inject_menus():
    return {'landing':LANDING_MENU['children'], 
            'login':LOGIN_MENU['children']}

