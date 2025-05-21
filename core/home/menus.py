
from flask_babel import lazy_gettext as _l
from core.utils import navbar, sidebar


navbar.add('home', _l('Accueil'), endpoint='home.index')
sidebar.add('home', _l('Accueil'), endpoint='home.dashboard', rank=-1)
sidebar.add('profile', _l('Profile'), rank=-1)
