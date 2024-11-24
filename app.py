
from core.config import app
from core.utils import register_api, register_ui, init_db


register_api()
register_ui()
init_db()

@app.route('/temp/<module>/<page>')
def temp(module, page):
    return f'no page "{page}" in module "{module}"'

