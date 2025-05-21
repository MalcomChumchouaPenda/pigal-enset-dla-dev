
from flask_babel import lazy_gettext as _l
from core.utils import navbar


# navbar.add_menu('msg_menu')
# navbar.add_menu('home_menu')
navbar.add('home', _l('Accueil'), endpoint='home.index')
