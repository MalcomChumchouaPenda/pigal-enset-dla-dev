
from flask import render_template
from core.utils import create_ui, add_entry, get_assets


ui = create_ui('home')
assets = get_assets('home')

add_entry('landing', 1, 'home', 'Accueil', point='home.index')
add_entry('landing', 2, 'courses', 'Formations', point='courses.index')
add_entry('landing', 3, 'research', 'Recherche', point='research.index')
add_entry('landing', 4, 'organisation', 'Organisation', point='organisation.index')
add_entry('landing', 5, 'landing-spaces', 'Espaces')
add_entry('landing', 6, 'contact', 'Contact', url="#contacts")
add_entry('landing-spaces', 1, 'events', 'Actualités', point='events.index')
add_entry('landing-spaces', 2, 'admission', 'Inscription', point='admission.index')
add_entry('landing-spaces', 3, 'project_a', 'Projet A', point='project_a.index')
add_entry('landing-spaces', 4, 'project_b', 'Projet B', point='project_b.index')
add_entry('login', 1, 'home', 'Accueil', point='home.index')
add_entry('login', 2, 'project_a', 'ProjetA', point='project_a.index')


@ui.route('/')
def index():
    heros = []
    for i in range(3):
        msg = assets.read_markdown(f'md/hero-msg-{i+1}.md')
        img = f'img/hero-bg-{i+1}.jpg'
        heros.append(dict(msg=msg, img=img))
    return render_template('home.html', heros=heros)

