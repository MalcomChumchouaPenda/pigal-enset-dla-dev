
from flask import render_template
from core.utils import create_ui, add_entry


ui = create_ui('home')
add_entry('landing', 1, 'home', 'Accueil', point='home.index')
add_entry('landing', 2, 'courses', 'Formations', point='courses.index')
add_entry('landing', 3, 'research', 'Recherche')
add_entry('landing', 5, 'team', 'Organisation')
add_entry('landing', 6, 'spaces', 'Espaces')
add_entry('landing', 7, 'contact', 'Contact')

add_entry('spaces', 1, 'events', 'Actualites', point='events.index')
add_entry('spaces', 2, 'students', 'Etudiants')
add_entry('spaces', 3, 'teachers', 'Enseignants')
add_entry('spaces', 4, 'staff', 'Administration')

# add_entry('sections', 1, 'hero1', 'Hero standard', point='demo.hero')
# add_entry('sections', 2, 'hero2', 'Hero large', point='demo.hero', kind='large')
# add_entry('sections', 3, 'hero3', 'Hero small', point='demo.hero', kind='small')
# add_entry('sections', 4, 'hero4', 'Hero carousel', point='demo.hero', kind='carousel')
# add_entry('sections', 5, 'about', 'About', point='demo.about')
# add_entry('sections', 6, 'services', 'Services', point='demo.services')
# add_entry('sections', 7, 'speechs', 'Speechs', point='demo.speechs')



@ui.route('/')
def index():
    return render_template('home.html')

