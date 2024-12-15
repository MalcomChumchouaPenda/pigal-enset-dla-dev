
from flask import render_template
from core.utils import create_ui, default_deadline


ui = create_ui('project_a')

@ui.route('/')
def index():
    return render_template('landing-coming-soon.html', 
                            title='Project A', 
                            deadline=default_deadline())
