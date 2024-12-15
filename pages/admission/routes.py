
from flask import render_template, request
from core.utils import create_ui
from services.demo import queries as qry


ui = create_ui('admission')


@ui.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title='Inscription termine'
        message="Votre inscription s'est terminee avec succes"
        return render_template('landing-confirmation.html', 
                               meta_title='Inscription',
                               title=title,
                               message=message)  
    # formations = qry.read_opened_formations()
    # niveaux = qry.read_niveaux() 
    pays = qry.get_pays()   
    professions = qry.get_professions()
    return render_template('admission.html', 
                           numero=1,
                           pays=pays,
                           professions=professions)

