# pigal-enset-dla-dev
Template pour le developpement de Portail d'Information et de Gestion des Activites academiques en ligne (Pigal) de l'ENSET de Douala. Ce template est destine au developpeurs qui souhaitent contribuer a la diffusion des informations et la gestion optimale des activites relatives a l'ENSET de Douala.

## Structure Générale
```
/pigal
│
├── /core                      # Noyau d'une app Pigal
│   ├── /auth                  # Microservice d'authentification (Blueprint)
│   ├── /home                  # Front-end d'accueil et d'authentification (Blueprint)
│   ├── /info                  # Microservice des infos generales (Blueprint)
│   ├── /store                 # Ressources dynamiques
│   ├── /themes                # Themes (static + templates)
│   ├── /utils                 # Fonctions et Classes utilitaires
│   ├── config.py              # Configuration de l'application Flask
│   ├── manifest.json          # documentation sur le core
│
├── /migrations                # Fichiers de migration pour SQLAlchemy
├── /plugins                   # Plugins ou modules d'une app Pigal
│   ├── /pages                 # Front-ends ou pages (Blueprints)
│   ├── /services              # Microservices ou APIs (Blueprints)
|
├── /tests                     # Tests unitaires et d'intégration
├── /translations              # Fichiers de translations
|
├── app.py                     # Point d'entrée principal pour l'app Pigal
├── requirements.txt           # Dépendances des templates Pigal
├── README.md                  # Documentation des templates Pigal
```

## Installation et Lancement
1. Cloner le dépôt :
   ```bash
   git clone <repo_url>
   cd pigal-enset-dla-dev
   ```
2. Créer et activer un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```
3. Installer les dépendances :
   ```bash
   python.exe -m pip install -r requirements.txt
   ```
4. Configurer l'application en creant un fichier `.env`:
   ```bash
   FLASK_ENV=development
   PIGAL_MYSQL_USER=demo
   PIGAL_MYSQL_PWD=demo
   
   ```

   ce fichier permet de configurer les variables suivantes:
   | VARIABLES | ROLES |
   |---|---|
   | PIGAL_MYSQL_USER  | compte utilisateur MySQL |
   | PIGAL_MYSQL_PWD  | Mot de passe MySQL |
   | PIGAL_SECRET_KEY | Cle secrete |


4. Lancer l'application :
   ```bash
   flask run
   ```


## Fonctionnalites

ce template permet de developper:
- des themes personnalises **themes**
- des **pages** permettant de developper des interfaces web ou frontends
- des **services** permettant de developper des API et des microservices

### Developpement des pages (plugins)

### Developpement des services (plugins)

