
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from core.config import db


# Association table for many-to-many relationship
user_roles = db.Table('user_roles',
    db.Column('user_id', db.String(100), db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.String(50), db.ForeignKey('role.id'), primary_key=True)
)

class Role(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.String(100), primary_key=True)
    lang = db.Column(db.String(3), nullable=True, default='fr')
    password_hash = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary=user_roles, 
                            backref=db.backref('users', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def has_role(self, role_id):
        for role in self.roles:
            if role.id == role_id:
                return True
        return False

    def has_roles(self, *role_ids):
        for role_id in role_ids:
            for role in self.roles:
                if role.id == role_id:
                    return True
        return False
    
    def filter_domains(self, services):
        """fonction pour protéger les services presentes sur l'accueil des dashboards."""
        filtered_groups = []
        for group in services:
            if 'roles' in group and not self.has_roles(*group['roles']):
                    continue
            filtered_services = []
            for service in group['services']: 
                if 'roles' in services and not self.has_roles(*service['roles']):
                        continue
                accepted_service = service.copy()
                filtered_services.append(accepted_service)
            if len(filtered_services) > 0:
                accepted_group = group.copy()            
                accepted_group['services'] = filtered_services
                filtered_groups.append(accepted_group)
        return filtered_groups

print('created models')