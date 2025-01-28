
from flask import Blueprint, render_template
from flask_login import login_required
from core.utils import roles_required


bp = Blueprint('project_c', __name__,
                url_prefix='/projets/c',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')

@bp.route('/')
@login_required
def index():
    return render_template('project-c.html')

@bp.route('/admin')
@login_required
@roles_required('admin', 'staff')
def admin():
    return render_template('project-c-admin.html')

@bp.route('/teacher')
@login_required
@roles_required('teacher')
def teacher():
    return render_template('project-c-teacher.html')

@bp.route('/student')
@login_required
@roles_required('student')
def student():
    return render_template('project-c-student.html')
