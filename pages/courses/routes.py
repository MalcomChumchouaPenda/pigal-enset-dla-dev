
from flask import render_template
from core.utils import create_ui, get_assets
from services.demo import queries as qry


ui = create_ui('courses')
assets = get_assets('courses')

@ui.route('/')
def index():
    return render_template('courses.html')
