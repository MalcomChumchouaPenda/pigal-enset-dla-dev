
from core.config import app
from core import utils as utl
from pages.landing.home import constants as cst
from pages.landing.main import MENU as LANDING_MENU


utl.register_api()
utl.init_db()


@app.context_processor
def inject_constants():
    return {'contact':cst.CONTACT,
            'links':cst.LINKS,
            'landing_entries':LANDING_MENU, 
            'login_entries':cst.LOGIN_MENU}

