
import os
import pytest
from flask import Flask
from core import config


@pytest.fixture
def test_app(tmp_path, monkeypatch):
    # Créer le fichier statique temporaire
    static_dir = tmp_path / "static"
    static_dir.mkdir()
    logo_path = static_dir / "logo.png"
    logo_path.write_bytes(b"\x89PNG\r\n\x1a\n")  # En-tête PNG factice

    os.environ['FLASK_ENV'] = 'testing'
    monkeypatch.setattr(config, 'THEMES_DIR', static_dir)
    app = config.create_app()
    yield app

@pytest.fixture
def test_client(test_app):
    return test_app.test_client()

def test_static_file_serving(test_client):
    response = test_client.get("/static/logo.png")
    assert response.status_code == 200
    assert response.mimetype == "image/png"
    assert response.data.startswith(b"\x89PNG")

