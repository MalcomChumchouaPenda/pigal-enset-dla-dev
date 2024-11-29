
from flask import render_template
from core.config import app, ENTRIES
from core.utils import register_api, register_ui
from core.utils import init_db
from core.utils import default_deadline


register_api()
register_ui()
init_db()


@app.route('/temp/<module>/<page>')
def temp(module, page):
    return f'no page "{page}" in module "{module}"'

@app.context_processor
def inject_entries():
    return {key:entry['children'] for key, entry in ENTRIES.items()}

@app.context_processor
def inject_defaults():
    return {'default_deadline':default_deadline}

@app.errorhandler(404)
def not_found(e):
    return render_template('error-404.html')
