
from flask import render_template
from core.config import app
from core.utils import create_ui, register_entry


ui = create_ui('home')


@ui.route('/')
def index():
    return render_template('home_index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('home-404.html')
