

from .schemas import Role, User


def init_data(session):
    roles = init_roles(session)
    init_users(session, roles)
    print("Demo users and roles created successfully!")


def init_roles(session):
    demo_roles = [
        {'id':'admin', 'name':'Responsable Administratif'},
        {'id':'staff', 'name':'Personnel Administratif'},
        {'id':'teacher', 'name':'Enseignant'},
        {'id':'student', 'name':'Etudiant'},
        {'id':'candidate', 'name':'Candidat'}
    ]
    roles = {}
    for demo in demo_roles:
        role = Role.query.filter_by(id=demo['id']).first()   
        if not role:
            role = Role(**demo)
            session.add(role)    
        roles[demo['id']] = role    
    session.commit()
    return roles

def init_users(session, roles):
    demo_users = [
        {'id':'demo1', 'name':'Responsable Test', 'password':'demo', 'role_ids':['admin']},
        {'id':'demo2', 'name':'Personnel Test', 'password':'demo', 'role_ids':['staff']},
        {'id':'demo3', 'name':'Enseignant Test', 'password':'demo', 'role_ids':['teacher']},
        {'id':'demo4', 'name':'Etudiant Test', 'password':'demo', 'role_ids':['student']},
        {'id':'demo5', 'name':'Candidat Test', 'password':'demo', 'role_ids':['candidate']}
    ]
    for demo in demo_users:
        user = User.query.filter_by(id=demo["id"]).first()
        if not user:
            user_roles = [roles[id_] for id_ in demo.pop('role_ids')]
            user = User(roles=user_roles, **demo)
            session.add(user)

    session.commit()
