
from flask_babel import lazy_gettext as _l
from core.utils import navbar, sidebar


navbar.add('home', _l('Accueil'), endpoint='home.index')
sidebar.add('home', _l('Accueil'), endpoint='home.dashboard')
test1 = sidebar.add('test1', 'Test1')
test1.add('test2', 'Test2')
