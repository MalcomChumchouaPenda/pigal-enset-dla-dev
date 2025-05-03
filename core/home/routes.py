
from flask import render_template, request, url_for, redirect
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from core.config import login_manager
from core.utils import UiBlueprint
from core.auth.tasks import connect_user, disconnect_user


ui = UiBlueprint(__name__)
ui.register_menu('msg_menu')
ui.register_menu('home_menu')
ui.register_entry('home_menu', 'home', _l('Accueil'), endpoint='home.index', rank=0)


@ui.route('/')
def index():
    return render_template('home.jinja')

class LoginForm(FlaskForm):
    id = StringField(_l('identifiant'), validators=[DataRequired()])
    pwd = PasswordField(_l('mot de passe'), validators=[DataRequired()])


@ui.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    next = request.args.get('next')
    if next is None:
        next = request.referrer
    if form.validate_on_submit():
        user_id = form.id.data
        password = form.pwd.data
        if connect_user(user_id, password):
            if next:
                return redirect(next)
            return redirect(url_for('home.index'))
        error = _("Informations incorrectes")
        return render_template('home-login.jinja', form=form, next=next, error=error)
    return render_template('home-login.jinja', form=form,  next=next)

@ui.route('/logout')
def logout():
    if current_user.is_authenticated:
        disconnect_user()
    return redirect(url_for('home.index'))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('home.login', next=request.path))


@ui.route('/denied')
def access_denied():
    msg = _("Vous n'avez pas les autorisations nécessaires pour accéder à cette page.")
    actions = [{'text':_("Revenir a l'accueil"), 'url':'/'}]
    prev = request.referrer
    if prev is not None:
        actions.append({'text':_("Revenir a la page precedente"), 'url':prev})
    return render_template('landing/error.jinja', number=403, actions=actions, message=msg), 403

