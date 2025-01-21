
import os
from core.config import app, PORTALS, PAGES_DIR, SERVICES_DIR
from core.utils import register_api, register_ui, init_db
from core.utils import read_markdown
from core.utils import default_deadline
from pages.home.constants import CONTACT, LINKS
from pages.home.constants import LANDING_MENU, LOGIN_MENU


register_api()
register_ui()
init_db()


@app.context_processor
def inject_defaults():
    return {'default_deadline':default_deadline, 
            'portals': PORTALS,
            'contact':CONTACT,
            'links':LINKS}

@app.context_processor
def inject_menus():
    return {'landing_entries':LANDING_MENU, 
            'login_entries':LOGIN_MENU}


@app.template_filter('safe_md')
def convert_to_safe(md_link):
    if '/store/' in md_link:
        md_dir = SERVICES_DIR
    elif '/assets/' in md_link:
        md_dir = PAGES_DIR
    else:
        raise RuntimeError(f'Invalid Path -> {md_link}')
    if md_link.startswith('/'):
        md_link = md_link[1:]
    md_link = os.path.normpath(md_link)
    filename = os.path.join(md_dir, md_link)
    safe = app.jinja_env.filters['safe']
    return safe(read_markdown(filename))

