
from core.utils import create_ui, render_coming_soon


ui = create_ui('project_a')

@ui.route('/')
def index():
    return render_coming_soon('Project A', 'landing')
