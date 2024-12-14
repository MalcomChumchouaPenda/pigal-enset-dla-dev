
from flask import render_template, request, redirect, url_for
from core.config import app, PORTALS
from core.utils import register_api, register_ui
from core.utils import init_db
from core.utils import default_deadline
from pages.home.constants import CONTACT, LINKS
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



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['portalId']
        return redirect(url_for('login_portal', id=id))
    return render_template('login-portals.html')


@app.route('/login/<id>', methods=['GET', 'POST'])
def login_portal(id):
    if request.method == 'POST':
        return 'Ok data'
    return render_template(f'login-{id}.html')



@app.context_processor
def inject_defaults():
    return {'default_deadline':default_deadline, 
            'portals': PORTALS,
            'contact':CONTACT,
            'links':LINKS}

@app.context_processor
def inject_menus():
    return {'landing':LANDING_MENU['children'], 
            'login':LOGIN_MENU['children']}

