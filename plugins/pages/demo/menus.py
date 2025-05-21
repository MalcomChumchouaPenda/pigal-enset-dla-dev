
from flask_babel import lazy_gettext as _l
from core.utils import navbar, sidebar


demomenu = navbar.add('demo_menu', _l('Demo'))
submenu1 = demomenu.add('sub_menu_1', _l('Pages'))
submenu2 = demomenu.add('sub_menu_2', _l('Sections'))
submenu3 = demomenu.add('sub_menu_3', _l('Dashboards'), rank=2)

submenu1.add('sub_menu_1_1', _l('Page vide'), endpoint='demo.blank', rank=0)
submenu1.add('sub_menu_1_3', _l('Page de message'), url='/demo/message', rank=1)
submenu1.add('sub_menu_1_4', _l('Page Attente'), endpoint='demo.coming_soon', rank=2)

submenu1.add('sub_menu_1_5_1', _l('Page avec hero large'), url='/demo/hero/lg', rank=3)
submenu1.add('sub_menu_1_5_2', _l('Page avec hero moyen'), url='/demo/hero/md', rank=3)
submenu1.add('sub_menu_1_5_3', _l('Page avec hero reduit'), url='/demo/hero/sm', rank=3)
submenu1.add('sub_menu_1_5_4', _l('Page avec hero carousel'), url='/demo/hero/carousel', rank=3)

submenu1.add('sub_menu_1_6_1', _l('Page avec footer large'), url='/demo/footer/lg', rank=4)
submenu1.add('sub_menu_1_6_2', _l('Page avec footer moyen'), url='/demo/footer/md', rank=4)
submenu1.add('sub_menu_1_6_3', _l('Page avec footer reduit'), url='/demo/footer/sm', rank=4)
submenu1.add('sub_menu_1_6_4', _l('Page avec footer avec auteurs'), url='/demo/footer/authors', rank=4)

submenu2.add('sub_menu_2_1', _l('Services'), endpoint='demo.services', rank=0)
submenu2.add('sub_menu_2_2', _l('About'), endpoint='demo.about', rank=1)
submenu2.add('sub_menu_2_3', _l('Recherche'), endpoint='demo.search', rank=2)
submenu2.add('sub_menu_2_4', _l('Evenements'), endpoint='demo.events', rank=3)
submenu2.add('sub_menu_2_5', _l('Attente'), endpoint='demo.coming_soon_sections', rank=4)

submenu3.add('sub_menu_3_1', _l('Dashboard (avec composants)'), endpoint='demo.dashboard', rank=0)
submenu3.add('sub_menu_3_2', _l('Dashboard (protege)'), endpoint='demo.protected', rank=1)
submenu3.add('sub_menu_3_3', _l('Dashboard (etudiants)'), endpoint='demo.student', rank=2)


formmenu = sidebar.add('form_menu', _l('Forms'))
formmenu.add('form_menu_1', _l('Form editors'), endpoint='demo.form_editors')
formmenu.add('form_menu_2', _l('Form elements'), endpoint='demo.form_elements')
formmenu.add('form_menu_3', _l('Form layouts'), endpoint='demo.form_layouts')
formmenu.add('form_menu_4', _l('Form validation'), endpoint='demo.form_validation')

datamenu = sidebar.add('data_menu', _l('Data'))
datamenu.add('data_menu_1', _l('General tables'), endpoint='demo.tables')
datamenu.add('data_menu_2', _l('Data tables'), endpoint='demo.datatables')
datamenu.add('data_menu_3', _l('Data charts'), endpoint='demo.charts')
