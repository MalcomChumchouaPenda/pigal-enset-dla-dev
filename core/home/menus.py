
from flask_babel import lazy_gettext as _l
from .routes import ui


ui.register_menu('msg_menu')
ui.register_menu('home_menu')
ui.register_entry('home_menu', 'home', _l('Accueil'), endpoint='home.index', rank=0)
