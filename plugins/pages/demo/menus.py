
from flask_babel import lazy_gettext as _l
from .routes import ui

ui.register_entry('home_menu', 'home_demo1', _l('Pages'))
ui.register_entry('home_menu', 'home_demo2', _l('Sections'))
ui.register_entry('home_menu', 'home_demo3', _l('Dashboards'), rank=2)


ui.register_entry('home_demo1', 'home_demo1_1', _l('Page vide'), endpoint='demo.blank', rank=0)
ui.register_entry('home_demo1', 'home_demo1_2', _l('Page avec menu'), endpoint='demo.menu', rank=1)
ui.register_entry('home_demo1', 'home_demo1_3', _l('Page de message'), url='/demo/message', rank=4)
ui.register_entry('home_demo1', 'home_demo1_4', _l('Page Attente'), endpoint='demo.coming_soon', rank=5)

ui.register_menu('demo_menu')
ui.register_entry('demo_menu', 'demo0', _l('Accueil'), endpoint='home.index', rank=0)
ui.register_entry('demo_menu', 'demo1', _l('Page 1'), url='#', rank=1)
ui.register_entry('demo_menu', 'demo2', _l('Page 2'), url='#', rank=2)
ui.register_entry('demo_menu', 'demo3', _l('Menus'), rank=3)
ui.register_entry('demo3', 'demo3_1', _l('Menu (ordonnee)'))
ui.register_entry('demo3', 'demo3_2', _l('Menu (reordonne)'))
ui.register_entry('demo3_1', 'demo3_1_1', _l('Page 1'), url='#')
ui.register_entry('demo3_1', 'demo3_1_2', _l('Page 2'), url='#')
ui.register_entry('demo3_2', 'demo3_2_1', _l('Page 1'), url='#', rank=1)
ui.register_entry('demo3_2', 'demo3_2_2', _l('Page 2'), url='#', rank=0)

ui.register_entry('home_demo1', 'home_demo1_5', _l('Page avec hero'), rank=2)
ui.register_entry('home_demo1_5', 'home_demo1_5_1', _l('Hero large'), url='/demo/hero/lg')
ui.register_entry('home_demo1_5', 'home_demo1_5_2', _l('Hero moyen'), url='/demo/hero/md')
ui.register_entry('home_demo1_5', 'home_demo1_5_3', _l('Hero reduit'), url='/demo/hero/sm')
ui.register_entry('home_demo1_5', 'home_demo1_5_4', _l('Hero carousel'), url='/demo/hero/carousel')

ui.register_entry('home_demo1', 'home_demo1_6', _l('Page avec footer'), rank=3)
ui.register_entry('home_demo1_6', 'home_demo1_6_1', _l('Footer large'), url='/demo/footer/lg', rank=0)
ui.register_entry('home_demo1_6', 'home_demo1_6_2', _l('Footer moyen'), url='/demo/footer/md', rank=1)
ui.register_entry('home_demo1_6', 'home_demo1_6_3', _l('Footer reduit'), url='/demo/footer/sm', rank=2)
ui.register_entry('home_demo1_6', 'home_demo1_6_4', _l('Footer avec auteurs'), url='/demo/footer/authors', rank=3)

ui.register_entry('home_demo2', 'home_demo2_1', _l('Services'), endpoint='demo.services', rank=0)
ui.register_entry('home_demo2', 'home_demo2_2', _l('About'), endpoint='demo.about', rank=1)
ui.register_entry('home_demo2', 'home_demo2_3', _l('Recherche'), endpoint='demo.search', rank=2)
ui.register_entry('home_demo2', 'home_demo2_4', _l('Evenements'), endpoint='demo.events', rank=3)
ui.register_entry('home_demo2', 'home_demo2_5', _l('Attente'), endpoint='demo.coming_soon_sections', rank=4)


ui.register_entry('home_demo3', 'home_demo3_1', _l('Dashboard (avec composants)'), endpoint='demo.dashboard', rank=0)
ui.register_entry('home_demo3', 'home_demo3_2', _l('Dashboard (protege)'), endpoint='demo.protected', rank=1)
ui.register_entry('home_demo3', 'home_demo3_3', _l('Dashboard (etudiants)'), endpoint='demo.student', rank=2)

ui.register_domain('g1',_l('Form Components'))
ui.register_dashboard('g1', 'd1', _l('Form editors'), endpoint='demo.form_editors')
ui.register_dashboard('g1', 'd2', _l('Form elements'), endpoint='demo.form_elements')
ui.register_dashboard('g1', 'd3', _l('Form layouts'), endpoint='demo.form_layouts')
ui.register_dashboard('g1', 'd4', _l('Form validation'), endpoint='demo.form_validation')

ui.register_domain('g2', _l('Data Components'))
ui.register_dashboard('g2', 'd4', _l('General tables'), endpoint='demo.tables')
ui.register_dashboard('g2', 'd5', _l('Data tables'), endpoint='demo.datatables')
ui.register_dashboard('g2', 'd6', _l('Data charts'), endpoint='demo.charts')
