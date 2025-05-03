
import os
import sys

test_dir = os.path.dirname(__file__)
root_dir = os.path.dirname(test_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)


import pytest
from core.config import db, create_app
from core.auth.defaults import init_data


@pytest.fixture
def app(monkeypatch):
    """Fixture qui crée une instance de l'application Flask pour les tests."""
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    with app.app_context():
        init_data()
    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Client de test Flask pour envoyer des requêtes API."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Fixture pour le CLI runner de Flask."""
    return app.test_cli_runner()
