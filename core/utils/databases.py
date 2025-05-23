
import os
import re
import inspect
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from .constants import (
    STORE_DIR, 
    TESTS_DIR, 
    SERVICES_DIR,
    SERVICE_NAME_PATTERN,
)


class ExtendedSQLAlchemy(SQLAlchemy):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.__bind_keys = []

    @classmethod
    def get_default_uri(cls, env_name):
        if env_name == 'testing':
            return "sqlite:///:memory:"
        if env_name == 'development':
            return f"sqlite:///{os.path.join(STORE_DIR, 'default.db')}"
        MYSQL_USER = os.getenv('PIGAL_MYSQL_USER')
        MYSQL_PWD = os.getenv('PIGAL_MYSQL_PWD')
        return f"mysql://{MYSQL_USER}:{MYSQL_PWD}@localhost/default"
    
    def get_binds(self, env_name):
        bind_keys = self._list_core_bind_keys()
        bind_keys.extend(self._list_plugins_bind_keys())
        bind_keys = list(set(bind_keys))
        binds = {}
        for bind_key in bind_keys:
            bind_uri = self._create_tenant_uri(env_name, bind_key)
            binds[bind_key] = bind_uri
        return binds

    @classmethod
    def _create_tenant_uri(cls, env_name, key):
        if env_name == 'testing':
            return f"sqlite:///{os.path.join(TESTS_DIR, 'data', key + '.db')}"
        if env_name == 'development':
            return f"sqlite:///{os.path.join(STORE_DIR, key + '.db')}"
        MYSQL_USER = os.getenv('PIGAL_MYSQL_USER')
        MYSQL_PWD = os.getenv('PIGAL_MYSQL_PWD')
        return f"mysql://{MYSQL_USER}:{MYSQL_PWD}@localhost/{key}"

    def _list_core_bind_keys(self):
        bind_keys = []
        for name in ['core.auth', 'core.info']:
            try:
                models = import_module(f'{name}.models')
                bind_keys.extend(self._list_bind_keys(models))
            except ModuleNotFoundError as e:
                pass
        return bind_keys
    
    def _list_plugins_bind_keys(self):
        bind_keys = []
        if os.path.isdir(SERVICES_DIR):
            for name in os.listdir(SERVICES_DIR):
                if not re.match(SERVICE_NAME_PATTERN, name):
                    continue
                modelspath = os.path.join(SERVICES_DIR, name, 'models.py')
                if not os.path.isfile(modelspath):
                    continue
                models = import_module(f'services.{name}.models')
                bind_keys.extend(self._list_bind_keys(models))
        return bind_keys

    def _list_bind_keys(self, models):
        bind_keys = []
        Model = self.Model
        for name, obj in inspect.getmembers(models):
            if inspect.isclass(obj) and issubclass(obj, Model) and obj != Model:
                bind_key = getattr(obj, '__bind_key__', None)
                if bind_key:
                    bind_keys.append(bind_key)
        return bind_keys

