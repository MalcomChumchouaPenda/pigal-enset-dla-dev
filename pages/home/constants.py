
from core.utils import create_menu

LANDING_MENU = create_menu()
LANDING_MENU.add_entry('home', 'Accueil', point='home.index')
LANDING_MENU.add_entry('courses', 'Formations', point='courses.index')
LANDING_MENU.add_entry('events', 'Actualités', point='events.index')
LANDING_MENU.add_entry('organisation', 'Organisation', point='organisation.index')
LANDING_MENU.add_entry('spaces', 'Espaces')
LANDING_MENU.add_entry('contact', 'Contact', url="#contacts")
LANDING_MENU.add_entry('admission', 'Inscription', point='admission.index', parent='spaces')
LANDING_MENU.add_entry('project_a', 'Projet A', point='project_a.index', parent='spaces')
LANDING_MENU.add_entry('project_b', 'Projet B', point='project_b.index', parent='spaces')

LOGIN_MENU = create_menu()
LOGIN_MENU.add_entry('home', 'Accueil', point='home.index')
LOGIN_MENU.add_entry('project_a', 'ProjetA', point='project_a.index')


CONTACT = {
    "addresse":"Campus Ndogbong, Universite de Douala",
    "ville":"Douala - Cameroun",
    "tel": "(+237) 699 99 99 99",
    "email": "cabenset@yahoo.fr",
    "twitter":"",
    "facebook":"",
    "instagram":"",
    "linkedin":""
}