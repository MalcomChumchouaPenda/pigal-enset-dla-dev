# Landing theme

Ce theme est destine au design des pages du site vitrine. Il contient:
- les `macros` utilisables dans ce theme
- le template de base `layout` pour toutes les pages
- le template `message` pour les pages d'info ou d'alerte
- le template `form` pour tous les formulaires
- le template `listing` pour toutes les pages de recherche
- le template `details` pour toutes les pages de details

## Les `macros`


## Le template `layout`

Ce template a 4 parties visibles:
- le block `page_header`
- le block `page_hero`
- le block `page_sections`
- le block `page_footer`

Le block `page_header` contient un block `page_menu`
Le block `page_footer` contient un block `page_authors`

Cette page est parametree par:
- la variable `footer-type` qui prend les valeurs (`sm`, `md`, `lg`)
