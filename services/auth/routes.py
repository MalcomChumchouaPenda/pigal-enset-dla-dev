
from core.utils import create_api


api = create_api('auth')


@api.route('/')
def info():
    return {'info':'Auth Api'}
