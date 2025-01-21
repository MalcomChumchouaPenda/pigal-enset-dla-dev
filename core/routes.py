
import os
from core.config import app, PAGES_DIR, SERVICES_DIR
from flask import render_template, request, redirect, url_for
from flask import send_from_directory


@app.route('/temp/<module>/<page>')
def temp(module, page):
    return f'no page "{page}" in module "{module}"'

@app.route('/<pname>/assets/<path:fname>')
def asset_file(pname, fname):
    pdir = os.path.join(PAGES_DIR, pname, 'assets')
    return send_from_directory(pdir, fname)

@app.route('/<sname>/store/<path:fname>')
def stored_file(sname, fname):
    pdir = os.path.join(SERVICES_DIR, sname, 'store')
    return send_from_directory(pdir, fname)


@app.errorhandler(404)
def not_found(e):
    print('\n', e)
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
        title = 'Connexion reussie'
        message = "La procedure d'authentification s'est terminee avec succes"
        actions = [{"text":"Aller a l'accueil", "point":"home.index"}]
        return render_template('login-confirmation.html',
                               title=title,
                               message=message,
                               actions=actions)
    return render_template(f'login-{id}.html')


@app.route('/login/<id>/recovering', methods=['GET', 'POST'])
def login_recovering(id):
    if request.method == 'POST':
        title = 'Recuperation terminee'
        message = "La procedure de recuperation s'est terminee avec succes"
        actions = [{"text":"Aller a l'accueil", "point":"home.index"}]
        return render_template('login-confirmation.html',
                               title=title,
                               message=message,
                               actions=actions)
    return render_template(f'login-{id}-recovering.html')

