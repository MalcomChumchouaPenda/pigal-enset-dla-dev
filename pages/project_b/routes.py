
from core.utils import create_ui, render_template


ui = create_ui('project_b')

@ui.route('/')
def index():
    return render_template('project-b.html')
