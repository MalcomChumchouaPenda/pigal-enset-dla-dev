
from flask import Blueprint
from .demo.routes import bp as demo_bp
from .demo import queries as demo_qry


DATA_CREATORS = [demo_qry.init_data]


api = Blueprint('api', __name__,
                url_prefix='/api',
                template_folder=None,
                static_folder=None)

api.register_blueprint(demo_bp)
