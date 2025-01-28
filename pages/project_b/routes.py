
from flask import Blueprint, render_template
from flask_security import auth_required

bp = Blueprint('project_b', __name__,
                url_prefix='/projets/b',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')

@bp.route('/')
@auth_required()
def index():
    return render_template('project-b.html')
