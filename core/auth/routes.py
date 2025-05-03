
from flask import request
from flask_login import current_user
from flask_restx import Resource, fields
from core.config import db, login_manager
from core.utils import ApiNamespace
from .models import User, Role
from .tasks import (
    connect_user, 
    disconnect_user,
    add_role,
    remove_role,
    add_roles_to_user,
    remove_roles_to_user
)


ns = ApiNamespace('auth', description="Systeme d'authentification")


credential_model = ns.model('credential', {
    'id': fields.String,
    'password': fields.String
})

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@ns.route('/login')
class LoginApi(Resource):

    @ns.expect(credential_model)
    def post(self):
        data = request.json
        if connect_user(data['id'], data['password']):
            return {'message': 'Logged in successfully'}, 200
        return {'message': 'Invalid credentials'}, 401

@ns.route('/logout')
class LogoutApi(Resource):
    def post(self):
        if current_user.is_authenticated:
            disconnect_user()
            return {'message': 'Logged out successfully'}, 200
        return {'message': 'User not logged in'}, 401


# API / USER ROUTES

user_model = ns.model('user', {
    'id': fields.String,
    'lang': fields.String
})


@ns.route('/users')
class UsersApi(Resource):

    @ns.marshal_list_with(user_model)
    def get(self):
        query = User.query
        role_id = request.args.get('role')
        if role_id:
            query = query.join(User.roles)
            query = query.filter(Role.id == role_id)
        return query.all()


@ns.route('/users/<user_id>')
class UserApi(Resource):

    @ns.marshal_with(user_model)
    @ns.doc('find_user')
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @ns.doc('add_user')
    def post(self, user_id):
        data = request.json
        pwd = data.pop('password')
        user = User(**data)
        user.id = user_id
        user.set_password(pwd)
        session = db.session
        session.add(user)
        session.commit()
        return {"message": "user added"}, 200

    @ns.doc('update_user')
    def put(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        data = request.json
        password = data.get('password')
        if password:
            user.set_password(password)

        lang = data.get('lang')
        if lang:
            user.lang = lang
        db.session.commit()
        return {"message": "user updated"}, 200

    @ns.doc('delete_user')
    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        session = db.session
        session.delete(user)
        session.commit()
        return "", 204


# API / ROLE ROUTES

role_model = ns.model("role", {
    "id": fields.String(required=True),
    "name": fields.String(required=True),
})

@ns.route("/roles")
class RolesApi(Resource):
    
    @ns.marshal_list_with(role_model)
    def get(self):
        roles = Role.query.all()
        return roles


    @ns.expect(role_model)
    @ns.roles_accepted('developper')
    def post(self):
        data = ns.payload
        add_role(db.session, data["id"], data["name"])
        return {"message": "Role added"}, 201


@ns.route("/roles/<int:id>")
class RoleApi(Resource):

    @ns.roles_accepted('developper')
    def delete(self, id):
        remove_role(db.session, id)
        return {"message": "Role deleted"}


@ns.route("/users/<int:user_id>/roles")
class UserRolesApi(Resource):

    @ns.roles_accepted('developper')
    def post(self, user_id):
        role_ids = ns.payload.get("role_ids", [])
        add_roles_to_user(db.session, user_id, *role_ids)
        return {"message": "Roles added to user"}

    @ns.roles_accepted('developper')
    def delete(self, user_id):
        role_ids = ns.payload.get("role_ids", [])
        remove_roles_to_user(db.session, user_id, *role_ids)
        return {"message": "Roles removed from user"}