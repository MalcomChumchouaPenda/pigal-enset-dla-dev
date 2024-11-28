
from flask import render_template
from core.utils import create_ui


ui = create_ui('admission')

@ui.route('/')
def index():
    return render_template('admission.html')