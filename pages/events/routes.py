
from flask import render_template
from core.utils import create_ui


ui = create_ui('events')

@ui.route('/')
def index():
    return render_template('events.html')

