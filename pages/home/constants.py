
LANDING_MENU = [
    {'uid':'home', 'text':'Accueil', 'point':'home.index'},
    {'uid':'courses', 'text':'Formations', 'point':'courses.index'},
    {'uid':'events', 'text':'Actualités', 'point':'events.index'},
    {'uid':'organisation', 'text':'Organisation', 'point':'organisation.index'},
    {'uid':'spaces', 'text':'Espaces', 'children':[
        {'uid':'admission', 'text':'Inscription', 'point':'admission.index'},
        {'uid':'project_a', 'text':'Projet A', 'point':'project_a.index'},
        {'uid':'project_b', 'text':'Projet B', 'point':'project_b.index'}
    ]},
    {'uid':'contact', 'text':'Contact', 'url':'#contact'}
]

LOGIN_MENU = [
    {'uid':'home', 'text':'Accueil', 'point':'home.index'},
    {'uid':'project_a', 'text':'Projet A', 'point':'project_a.index'}
]

CONTACT = {
    "addresse":"Campus Ndogbong, Universite de Douala",
    "ville":"Douala - Cameroun",
    "tel": "(+237) 699 99 99 99",
    "email": "cabenset@yahoo.fr",
    "twitter":"",
    "facebook":"",
    "instagram":"",
    "linkedin":""
}

LINKS = [
    {
        "group":"Liens Utiles",
        "links":[
            {"url":"#", "nom":"Universite de Douala"},
            {"url":"#", "nom":"Systhag Online"},
            {"url":"#", "nom":"Ministere de l'Enseignement Superieur"}
        ]
    }
]
