
from flask import render_template, request
from core.utils import create_ui
from services.demo import queries as qry


ui = create_ui('admission')

@ui.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'Hello world'
        # return render_template('confirmation.html', dossier=dossier)     
    # formations = qry.read_opened_formations()
    # niveaux = qry.read_niveaux() 
    pays = qry.get_pays()   
    professions = qry.get_professions()
    return render_template('admission.html', 
                           numero=1,
                           pays=pays,
                           professions=professions)

