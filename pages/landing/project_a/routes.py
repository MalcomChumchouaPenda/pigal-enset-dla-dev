
from flask import Blueprint, render_template
from core.utils import default_deadline


bp = Blueprint('project_a', __name__,
                url_prefix='/projets/a',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')

@bp.route('/')
def index():
    return render_template('landing-coming-soon.html', 
                            title='Project A', 
                            deadline=default_deadline())
