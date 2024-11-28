
from flask import render_template
from core.utils import create_ui, add_entry


ui = create_ui('home')
add_entry('landing', 1, 'home', 'Accueil', point='home.index')
add_entry('landing', 2, 'courses', 'Formations', point='courses.index')
add_entry('landing', 3, 'research', 'Recherche', point='research.index')
add_entry('landing', 4, 'organisation', 'Organisation', point='organisation.index')
add_entry('landing', 5, 'landing-spaces', 'Espaces')
add_entry('landing', 6, 'contact', 'Contact', url="#contacts")
add_entry('landing-spaces', 1, 'events', 'Actualités', point='events.index')
add_entry('landing-spaces', 2, 'admission', 'Inscription', point='admission.index')
add_entry('landing-spaces', 3, 'project', 'Projet', point='project.index')

add_entry('login', 1, 'home', 'Accueil', point='home.index')
add_entry('login', 5, 'project', 'Projet', point='project.index')


@ui.route('/')
def index():
    return render_template('home.html')

