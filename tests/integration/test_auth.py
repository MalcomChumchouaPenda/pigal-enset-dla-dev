
import json
import pytest
from flask import jsonify
from flask_restx import Resource
from core.utils import ApiNamespace
from core.config import db, api
from core.auth.models import User


def test_login_success(client):
    """Test de connexion réussie avec des identifiants valides."""
    response = client.post('/api/auth/login', json={"id": "admin1", "password": "adminpass"})
    assert response.status_code == 200
    assert response.json["message"] == "Logged in successfully"

def test_login_failure(client):
    """Test de connexion échouée avec un mauvais mot de passe."""
    response = client.post('/api/auth/login', json={"id": "admin1", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json["message"] == "Invalid credentials"

def test_logout(client):
    """Test de déconnexion après une connexion réussie."""
    client.post('/api/auth/login', json={"id": "admin1", "password": "adminpass"})
    response = client.post('/api/auth/logout')
    assert response.status_code == 200
    assert response.json["message"] == "Logged out successfully"



@pytest.fixture
def ns(app):
    """Api pour test des privileges"""
    ns = ApiNamespace('demo')

    @ns.route('/some_protected_route')
    class TestApi1(Resource):
        @ns.login_required
        def get(self):
            return {'message': 'Hi'}, 200

    @ns.route('/admin/protected')
    class TestApi2(Resource):
        @ns.roles_accepted('admin')
        def get(self):
            return {'message': 'Hi admin'}, 200
        
    @ns.route('/teacher/protected')
    class TestApi3(Resource):
        @ns.roles_accepted('teacher')
        def get(self):
            return {'message': 'Hi teacher'}, 200
        
    @ns.route('/student/protected')
    class TestApi4(Resource):
        @ns.roles_accepted('student')
        def get(self):
            return {'message': 'Hi student'}, 200
        
    @ns.route('/multiple-roles/protected')
    class TestApi5(Resource):
        @ns.roles_accepted('student', 'teacher')
        def get(self):
            return {'message': 'Hi user'}, 200

    api.add_namespace(ns, path='/test')
    return ns


def test_protected_route_without_login(client, ns):
    """Test d'accès à une route protégée sans connexion."""
    response = client.get('/api/test/some_protected_route')
    assert response.status_code == 401

def test_admin_access(client, ns):
    """Test d'accès à une route réservée aux admins."""
    client.post('/api/auth/login', json={"id": "admin1", "password": "adminpass"})
    response = client.get('/api/test/admin/protected')
    assert response.status_code == 200

def test_teacher_access(client, ns):
    """Test d'accès à une route réservée aux enseignants."""
    client.post('/api/auth/login', json={"id": "teacher1", "password": "teacherpass"})
    response = client.get('/api/test/teacher/protected')
    assert response.status_code == 200

def test_student_access(client, ns):
    """Test d'accès à une route réservée aux etudiants."""
    client.post('/api/auth/login', json={"id": "student1", "password": "studentpass"})
    response = client.get('/api/test/student/protected')
    assert response.status_code == 200

@pytest.mark.parametrize("name,pwd", [('teacher1', 'teacherpass'), ('student1', 'studentpass')])
def test_multiple_role_access(client, ns, name, pwd):
    """Test d'accès à une route réservée a plusieurs roles."""
    client.post('/api/auth/login', json={"id": name, "password": pwd})
    response = client.get('/api/test/multiple-roles/protected')
    assert response.status_code == 200

@pytest.mark.parametrize("name,pwd", [('teacher1', 'teacherpass'), ('student1', 'studentpass')])
def test_user_forbidden(client, ns, name, pwd):
    """Test qu'un utilisateur ne peut pas accéder à une route protege."""
    client.post('/api/auth/login', json={"id": name, "password": pwd})
    response = client.get('/api/test/admin/protected')
    assert response.status_code == 403


def test_get_users(client):
    response = client.get("/api/auth/users")
    assert response.status_code == 200
    assert len(response.json) == 4

def test_get_users_by_role(client):
    response = client.get("/api/auth/users?role=teacher")
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_user_by_id(client):
    response = client.get("/api/auth/users/teacher1")
    assert response.status_code == 200
    user = response.json
    assert user['id'] == 'teacher1'

def test_add_user(client, app):
    data = {"lang":"fr", "password":"test"}
    response = client.post("/api/auth/users/test1", 
                            data=json.dumps(data), 
                            content_type="application/json")
    
    assert response.status_code == 200
    assert "user added" in response.json["message"]
    with app.app_context():
        user = db.session.query(User).filter_by(id='test1').one()
        assert user.lang == "fr"
        assert user.check_password("test")
    
def test_update_user_password(client, app):
    data = {"password":"test"}
    response = client.put("/api/auth/users/teacher1", 
                            data=json.dumps(data), 
                            content_type="application/json")
    
    assert response.status_code == 200
    assert "user updated" in response.json["message"]
    with app.app_context():
        user = db.session.query(User).filter_by(id='teacher1').one()
        assert user.check_password("test")
        assert user.lang == "fr"

def test_update_user_lang(client, app):
    data = {"lang":"en"}
    response = client.put("/api/auth/users/teacher1", 
                          data=json.dumps(data), 
                          content_type="application/json")
    
    assert response.status_code == 200
    assert "user updated" in response.json["message"]
    user = db.session.query(User).filter_by(id='teacher1').one()
    assert user.check_password("teacherpass")
    assert user.lang == "en"

def test_delete_user(client):
    response = client.delete("/api/auth/users/teacher1")
    assert response.status_code == 204


@pytest.mark.parametrize("name,pwd,code", [
    ('dev1', 'devpass', 201), 
    ('admin1', 'adminpass', 403)
    ])
def test_add_role(client, name, pwd, code):
    client.post('/api/auth/login', json={"id": name, "password": pwd})
    response = client.post("/api/auth/roles", json={"id": '1', "name": "Editor"})
    assert response.status_code == code


@pytest.mark.parametrize("name,pwd,code", [
    ('dev1', 'devpass', 200), 
    ('admin1', 'adminpass', 403)
    ])
def test_remove_role(client, name, pwd, code):
    client.post('/api/auth/login', json={"id": name, "password": pwd})
    client.post("/api/auth/roles", json={"id": '2', "name": "Editor"})
    response = client.delete("/api/auth/roles/2")
    assert response.status_code == code


@pytest.mark.parametrize("name,pwd,code", [
    ('dev1', 'devpass', 200), 
    ('admin1', 'adminpass', 403)
    ])
def test_add_roles_to_user(client, name, pwd, code):
    client.post('/api/auth/login', json={"id": name, "password": pwd})
    client.post("/api/auth/roles", json={"id": '3', "name": "User"})
    response = client.post("/api/auth/users/1/roles", json={"role_ids": [3]})
    assert response.status_code == code


@pytest.mark.parametrize("name,pwd,code", [
    ('dev1', 'devpass', 200), 
    ('admin1', 'adminpass', 403)
    ])
def test_remove_roles_from_user(client, name, pwd, code):
    client.post('/api/auth/login', json={"id": name, "password": pwd})
    client.post("/api/auth/roles", json={"id": '4', "name": "Viewer"})
    client.post("/api/auth/users/2/roles", json={"role_ids": ['4']})
    response = client.delete("/api/auth/users/2/roles", json={"role_ids": ['4']})
    assert response.status_code == code
