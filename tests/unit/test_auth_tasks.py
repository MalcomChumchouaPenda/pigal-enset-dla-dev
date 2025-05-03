import pytest
from core.config import db
from core.auth.models import User, Role
from core.auth.tasks import (
    add_role, 
    remove_role, 
    add_roles_to_user, 
    remove_roles_to_user
)


@pytest.fixture
def user():
    user = User(id='1', password_hash="alice")
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def roles():
    role1 = Role(id='1', name="admin")
    role2 = Role(id='2', name="editor")
    db.session.add_all([role1, role2])
    db.session.commit()
    return [role1, role2]

def test_add_role(app):
    add_role(db.session, '3', "moderator")
    role = Role.query.get('3')
    assert role is not None
    assert role.name == "moderator"

def test_remove_role(app):
    add_role(db.session, '4', "temp")
    remove_role(db.session, '4')
    role = Role.query.get('4')
    assert role is None

def test_add_roles_to_user(app, user, roles):
    add_roles_to_user(db.session, user.id, '1', '2')
    user = User.query.get(user.id)
    role_ids = [role.id for role in user.roles]
    assert set(role_ids) == {'1', '2'}

def test_remove_roles_to_user(app, user, roles):
    add_roles_to_user(db.session, user.id, '1', '2')
    remove_roles_to_user(db.session, user.id, '1')
    user = User.query.get(user.id)
    remaining_ids = [role.id for role in user.roles]
    assert remaining_ids == ['2']
