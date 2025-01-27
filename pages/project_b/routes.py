
from flask import Blueprint, render_template


bp = Blueprint('project_b', __name__,
                url_prefix='/projets/b',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')

@bp.route('/')
def index():
    return render_template('project-b.html')
