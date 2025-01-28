
import os
from flask import render_template, request, redirect
from flask import url_for, send_from_directory, flash
from flask_login import login_user, logout_user, login_required
from urllib.parse import urlparse, urljoin
from .config import app, login_manager
from .config import PAGES_DIR, SERVICES_DIR
from .schemas import User
from .utils import default_deadline



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


# @app.errorhandler(404)
# def not_found(e):
#     print('\n', e)
#     message = "La page que vous recherchez n'existe plus"
#     actions = [{"text":"Retour a l'accueil", "url":"/"}]
#     return render_template('base-error.html',
#                            number=404,
#                            message=message,
#                            actions=actions)
def is_safe_url(target):
    """Check if the redirect target is a safe URL (same host)."""
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@login_manager.user_loader
def load_user(user_id):
    """Load user from database by ID."""
    return User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.args.get('next')
    if request.method == 'POST':
        user_id = request.form.get('userId')
        password = request.form.get('userPwd')
        user = User.query.filter_by(id=user_id).first()
        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            if next_page and is_safe_url(next_page):
                return redirect(next_page)
            return redirect(url_for('home.index'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login-user.html', next_page=next_page)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'info')
    return redirect(url_for('home.index'))


@app.route('/recovering')
def recovering():
    return render_template('landing-coming-soon.html', 
                            title='Recuperation Mot de passe', 
                            deadline=default_deadline())



# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return f"Welcome {current_user.id}, Roles: {[role.name for role in current_user.roles]}"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         id = request.form['portalId']
#         return redirect(url_for('login_portal', id=id))
#     return render_template('login-portals.html')


# @app.route('/login/<id>', methods=['GET', 'POST'])
# def login_portal(id):
#     if request.method == 'POST':
#         title = 'Connexion reussie'
#         message = "La procedure d'authentification s'est terminee avec succes"
#         actions = [{"text":"Aller a l'accueil", "url":"/"}]
#         return render_template('login-confirmation.html',
#                                title=title,
#                                message=message,
#                                actions=actions)
#     return render_template(f'login-{id}.html')


# @app.route('/login/<id>/recovering', methods=['GET', 'POST'])
# def login_recovering(id):
#     if request.method == 'POST':
#         title = 'Recuperation terminee'
#         message = "La procedure de recuperation s'est terminee avec succes"
#         actions = [{"text":"Aller a l'accueil", "url":"/"}]
#         return render_template('login-confirmation.html',
#                                title=title,
#                                message=message,
#                                actions=actions)
#     return render_template(f'login-{id}-recovering.html')

