
LANDING_MENU = [
    {'uid':'home', 'text':'Accueil', 'url':'/'},
    {'uid':'courses', 'text':'Formations', 'url':'/formations'},
    {'uid':'events', 'text':'Actualités', 'url':'/actualites'},
    {'uid':'organisation', 'text':'Organisation', 'url':'/organisation'},
    {'uid':'spaces', 'text':'Espaces', 'children':[
        {'uid':'admission', 'text':'Inscription', 'url':'/inscription'},
        {'uid':'project_a', 'text':'Projet A', 'url':'/projets/a'},
        {'uid':'project_b', 'text':'Projet B', 'url':'/projets/b'}
    ]},
    {'uid':'contact', 'text':'Contact', 'url':'#contact'}
]

LOGIN_MENU = [
    {'uid':'home', 'text':'Accueil', 'url':'/'},
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
