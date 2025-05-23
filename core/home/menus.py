
from flask_babel import lazy_gettext as _l
from core.utils import navbar, sidebar


navbar.add('home_pg', _l('Accueil'), endpoint='home.index')
workspacemenu = navbar.add('space_menu', _l('Espaces'))
workspacemenu.add('student_dash', _l('Etudiants'), endpoint='home.student_dashboard')
workspacemenu.add('teacher_dash', _l('Enseignants'), endpoint='home.teacher_dashboard')
workspacemenu.add('admin_dash', _l('Administration'), endpoint='home.admin_dashboard')

sidebar.add('home_dash', _l('Accueil'), endpoint='home.dashboard', rank=-1)
sidebar.add('profile_dash', _l('Profile'), endpoint='home.profile', rank=-1)
