
from flask import Blueprint, render_template, request
from core.config import db
from services.demo import queries as qry


bp = Blueprint('admission', __name__,
                url_prefix='/inscription',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title='Inscription termine'
        message="Votre inscription s'est terminee avec succes"
        return render_template('landing-confirmation.html', 
                               meta_title='Inscription',
                               title=title,
                               message=message)  
    pays = qry.get_pays(db.session)   
    professions = qry.get_professions(db.session)
    return render_template('admission.html', 
                           numero=1,
                           pays=pays,
                           professions=professions)

