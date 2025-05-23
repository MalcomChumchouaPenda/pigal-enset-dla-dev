
from flask_babel import lazy_gettext as _l
from core.utils import navbar, sidebar


navbar.add('home_pg', _l('Accueil'), endpoint='home.index')
sidebar.add('home_dash', _l('Accueil'), endpoint='home.dashboard', rank=-1)
sidebar.add('profile_dash', _l('Profile'), rank=-1)

# sidebar.add('home_dash', _l('Accueil'), endpoint='home.dashboard', rank=-1, icon="bi bi-house-fill")
# sidebar.add('profile_dash', _l('Profile'), rank=-1, icon="bi bi-person-circle")