
from flask import Blueprint, render_template


bp = Blueprint('organisation', __name__,
                url_prefix='/organisation',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')

@bp.route('/')
def index():
    return render_template('organisation.html')
