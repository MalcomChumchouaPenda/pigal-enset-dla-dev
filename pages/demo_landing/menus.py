
from flask_babel import lazy_gettext as _l
from core.utils import navbar


demomenu = navbar.add('demo_menu', _l('Demo'))
submenu1 = demomenu.add('sub_menu_1', _l('Pages'))
submenu2 = demomenu.add('sub_menu_2', _l('Sections'))
submenu3 = demomenu.add('sub_menu_3', _l('Dashboards'), rank=2)

submenu1.add('blank_pg', _l('Page vide'), endpoint='demo_landing.blank', rank=0)
submenu1.add('msg_pg', _l('Page de message'), url='/demo-landing/message', rank=1)
submenu1.add('coming_pg', _l('Page Attente'), endpoint='demo_landing.coming_soon', rank=2)

submenu1.add('hero_lg_pg', _l('Page avec hero large'), url='/demo-landing/hero/lg', rank=3)
submenu1.add('hero_md_pg', _l('Page avec hero moyen'), url='/demo-landing/hero/md', rank=3)
submenu1.add('hero_sm_pg', _l('Page avec hero reduit'), url='/demo-landing/hero/sm', rank=3)
submenu1.add('hero_carousel_pg', _l('Page avec hero carousel'), url='/demo-landing/hero/carousel', rank=3)

submenu1.add('footer_lg_pg', _l('Page avec footer large'), url='/demo-landing/footer/lg', rank=4)
submenu1.add('footer_md_pg', _l('Page avec footer moyen'), url='/demo-landing/footer/md', rank=4)
submenu1.add('footer_sm_pg', _l('Page avec footer reduit'), url='/demo-landing/footer/sm', rank=4)
submenu1.add('footer_authors_pg', _l('Page avec footer avec auteurs'), url='/demo-landing/footer/authors', rank=4)

submenu2.add('services_pg', _l('Services'), endpoint='demo_landing.services', rank=0)
submenu2.add('about_pg', _l('About'), endpoint='demo_landing.about', rank=1)
submenu2.add('search_pg', _l('Recherche'), endpoint='demo_landing.search', rank=2)
submenu2.add('events_pg', _l('Evenements'), endpoint='demo_landing.events', rank=3)
submenu2.add('coming_section_pg', _l('Attente'), endpoint='demo_landing.coming_soon_sections', rank=4)
