
from core.config import ma, login_manager
from .models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field()
    lang = ma.auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)


