
from core.config import db
from .models import User, Role


def init_data():
    # db.create_all()
    if not Role.query.first():
        roles = [
            Role(id='admin', name='Admin'),
            Role(id='teacher', name='Teacher'),
            Role(id='student', name='Student'),
            Role(id='developper', name='Developper')
        ]
        db.session.add_all(roles)
        db.session.commit()
    
    if not User.query.first():
        users_data = [
            dict(id='admin1', name='Admin', pwd='adminpass', role='admin'),
            dict(id='teacher1', name='Teacher', pwd='teacherpass', role='teacher'),
            dict(id='student1', name='Student', pwd='studentpass', role='student'),
            dict(id='dev1', name='Developper', pwd='devpass', role='developper'),
        ]
        for row in users_data:
            role = Role.query.filter_by(id=row['role']).one()
            user = User(id=row['id'], last_name=row['name'], roles=[role])
            user.set_password(row['pwd'])
            db.session.add(user)
        db.session.commit()
        