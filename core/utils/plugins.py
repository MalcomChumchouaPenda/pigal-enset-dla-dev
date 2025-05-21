
import os
import re
from functools import wraps
from flask import Blueprint
from flask import redirect, url_for
from flask_login import current_user, login_required
from flask_restx import Namespace
from .constants import ROOT_DIR




class UiBlueprint(Blueprint):

    def __init__(self, import_name, **kwargs):
        names = re.findall('.*\.([A-Za-z0-9_]+)\.routes', import_name)
        url_parts = import_name.split('.')
        url_parts[-1] = 'static'
        url_path = os.path.join(ROOT_DIR, *url_parts)
        super().__init__(names[0], import_name, 
                         template_folder='templates', 
                         static_folder='static',
                         static_url_path=url_path,
                        #  static_url_path='./static' ,
                         **kwargs)
        # print(import_name, self._static_url_path)
        self.login_required = login_required
        self.domains = {}
        

    def roles_accepted(self, *roles):
        """Décorateur pour protéger les routes Flask qui renvoient des pages HTML."""
        def decorator(f):
            @wraps(f)
            @login_required
            def decorated_function(*args, **kwargs):
                if not current_user.is_authenticated:
                    # Redirection vers la page de connexion
                    msg = "Vous devez être connecté pour accéder à cette page."
                    return redirect(url_for('home.login', message=msg))  
                if len([n for n in roles if current_user.has_role(n)]) == 0:
                     # Redirection vers la page d'accueil
                    msg = "Vous n'avez pas la permission d'accéder à cette page."
                    return redirect(url_for('home.access_denied', message=msg)) 
                return f(*args, **kwargs)
            return decorated_function
        return decorator
    

class ApiNamespace(Namespace):

    @classmethod
    def login_required(cls, f):
        """Décorateur pour protéger les routes API."""
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return {'message': 'Unauthorized'}, 401
            return f(*args, **kwargs)
        return decorated_function
    
    @classmethod
    def roles_accepted(cls, *roles):
        """Décorateur pour protéger les routes API avec des rôles spécifiques."""
        def decorator(f):
            @wraps(f)
            # @login_required
            def decorated_function(*args, **kwargs):
                if not current_user.is_authenticated:
                    return {'message': 'Unauthorized'}, 401
                if len([n for n in roles if current_user.has_role(n)]) == 0:
                    return {'message': 'Forbidden'}, 403
                return f(*args, **kwargs)
            return decorated_function
        return decorator
