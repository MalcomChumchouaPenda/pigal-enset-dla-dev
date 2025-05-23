
from flask_babel import lazy_gettext as _l
from core.utils import navbar, sidebar


demomenu = navbar.add('demo_menu', _l('Demo'))
submenu1 = demomenu.add('sub_menu_1', _l('Pages'))
submenu2 = demomenu.add('sub_menu_2', _l('Sections'))
submenu3 = demomenu.add('sub_menu_3', _l('Dashboards'), rank=2)

submenu1.add('blank_pg', _l('Page vide'), endpoint='demo.blank', rank=0)
submenu1.add('msg_pg', _l('Page de message'), url='/demo/message', rank=1)
submenu1.add('coming_pg', _l('Page Attente'), endpoint='demo.coming_soon', rank=2)

submenu1.add('hero_lg_pg', _l('Page avec hero large'), url='/demo/hero/lg', rank=3)
submenu1.add('hero_md_pg', _l('Page avec hero moyen'), url='/demo/hero/md', rank=3)
submenu1.add('hero_sm_pg', _l('Page avec hero reduit'), url='/demo/hero/sm', rank=3)
submenu1.add('hero_carousel_pg', _l('Page avec hero carousel'), url='/demo/hero/carousel', rank=3)

submenu1.add('footer_lg_pg', _l('Page avec footer large'), url='/demo/footer/lg', rank=4)
submenu1.add('footer_md_pg', _l('Page avec footer moyen'), url='/demo/footer/md', rank=4)
submenu1.add('footer_sm_pg', _l('Page avec footer reduit'), url='/demo/footer/sm', rank=4)
submenu1.add('footer_authors_pg', _l('Page avec footer avec auteurs'), url='/demo/footer/authors', rank=4)

submenu2.add('services_pg', _l('Services'), endpoint='demo.services', rank=0)
submenu2.add('about_pg', _l('About'), endpoint='demo.about', rank=1)
submenu2.add('search_pg', _l('Recherche'), endpoint='demo.search', rank=2)
submenu2.add('events_pg', _l('Evenements'), endpoint='demo.events', rank=3)
submenu2.add('coming_section_pg', _l('Attente'), endpoint='demo.coming_soon_sections', rank=4)

# submenu3.add('sub_menu_3_1', _l('Dashboard (avec composants)'), endpoint='demo.dashboard', rank=0)
# submenu3.add('sub_menu_3_2', _l('Dashboard (protege)'), endpoint='demo.protected', rank=1)
# submenu3.add('sub_menu_3_3', _l('Dashboard (etudiants)'), endpoint='demo.student', rank=2)


formmenu = sidebar.add('form_menu', _l('Forms'))
formmenu.add('form_editors_pg', _l('Form editors'), endpoint='demo.form_editors')
formmenu.add('form_elements_pg', _l('Form elements'), endpoint='demo.form_elements')
formmenu.add('form_layouts_pg', _l('Form layouts'), endpoint='demo.form_layouts')
formmenu.add('form_validation_pg', _l('Form validation'), endpoint='demo.form_validation')

datamenu = sidebar.add('data_menu', _l('Data'))
datamenu.add('tables_pg', _l('General tables'), endpoint='demo.tables')
datamenu.add('datatables_pg', _l('Data tables'), endpoint='demo.datatables')
datamenu.add('charts_pg', _l('Data charts'), endpoint='demo.charts')
