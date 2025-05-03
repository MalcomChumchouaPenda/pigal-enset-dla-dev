
from flask import current_app
from flask_login import login_user, logout_user
from flask_principal import Identity, AnonymousIdentity, identity_changed
from core.config import db
from .models import User


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

