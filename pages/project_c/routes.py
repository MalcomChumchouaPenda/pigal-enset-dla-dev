
from flask import Blueprint, render_template
from flask_login import login_required


bp = Blueprint('project_c', __name__,
                url_prefix='/projets/c',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')

@bp.route('/')
@login_required
def index():
    return render_template('project-c.html')
