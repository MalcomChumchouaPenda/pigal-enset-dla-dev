
from flask import request
from flask_login import current_user
from flask_restx import Namespace, Resource, fields
from core.config import db, login_manager
from .models import User, Role
from .tasks import connect_user, disconnect_user


ns = Namespace('auth', description="Systeme d'authentification")


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@ns.route('/login')
class LoginApi(Resource):
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

