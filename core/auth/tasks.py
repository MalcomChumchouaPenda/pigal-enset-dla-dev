
from flask import current_app
from flask_login import login_user, logout_user
from flask_principal import Identity, AnonymousIdentity, identity_changed
from core.config import db
from .models import User, Role


def connect_user(userid, pwd):
    session = db.session
    user = session.query(User).filter_by(id=userid).first()
    if user and user.check_password(pwd):
        login_user(user)
        identity_changed.send(
            current_app._get_current_object(), 
            identity=Identity(user.id)
        )
        return True
    return False

def disconnect_user():
    logout_user()
    identity_changed.send(
        current_app._get_current_object(), 
        identity=AnonymousIdentity()
    )
    return True

def add_role(session, id, name):
    if not Role.query.get(id):
        role = Role(id=id, name=name)
        session.add(role)
        session.commit()

def remove_role(session, id):
    role = Role.query.get(id)
    if role:
        session.delete(role)
        session.commit()

def add_roles_to_user(session, userid, *role_ids):
    user = User.query.get(userid)
    if user:
        for role_id in role_ids:
            role = Role.query.get(role_id)
            if role and role not in user.roles:
                user.roles.append(role)
        session.commit()

def remove_roles_to_user(session, userid, *role_ids):
    user = User.query.get(userid)
    if user:
        for role_id in role_ids:
            role = Role.query.get(role_id)
            if role and role in user.roles:
                user.roles.remove(role)
        session.commit()

