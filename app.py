
from core.config import app
from core import utils as utl
from pages.home import constants as cst


utl.register_api()
utl.register_ui()
utl.init_db()


@app.context_processor
def inject_constants():
    return {'contact':cst.CONTACT,
            'links':cst.LINKS,
            'landing_entries':cst.LANDING_MENU, 
            'login_entries':cst.LOGIN_MENU}

