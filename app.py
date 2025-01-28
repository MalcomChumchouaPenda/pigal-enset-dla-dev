
from core.config import app
from core.utils import init_db
from pages.home import constants as cst
from pages.main import MENU as LANDING_MENU
from services.main import api, DATA_CREATORS


app.register_blueprint(api)          # important ne pas modifier
init_db(DATA_CREATORS)

@app.context_processor
def inject_constants():
    return {'contact':cst.CONTACT,
            'links':cst.LINKS,
            'landing_entries':LANDING_MENU, 
            'login_entries':cst.LOGIN_MENU}

