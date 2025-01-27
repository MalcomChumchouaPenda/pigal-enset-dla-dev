
from core.config import app
from flask import Blueprint
from .demo.routes import bp as demo_bp


api = Blueprint('api', __name__,
                url_prefix='/api',
                template_folder=None,
                static_folder=None)


app.register_blueprint(api)          # important ne pas modifier
api.register_blueprint(demo_bp)
