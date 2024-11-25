
from core.utils import create_api


api = create_api('demo')


@api.route('/')
def root():
    return {'info':'Demo Api'}
