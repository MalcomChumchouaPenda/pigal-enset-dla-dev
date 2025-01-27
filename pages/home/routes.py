
from flask import Blueprint, render_template
from core.utils import get_assets
from core.config import db
from services.demo import queries as qry


assets = get_assets('home')
bp = Blueprint('home', __name__,
                url_prefix='/',
                template_folder='layouts',
                static_folder='assets',
                static_url_path='/assets')


@bp.route('/')
def index():
    speech = '/home/assets/md/speech.md'
    left = '/home/assets/md/about-left.md'
    right = '/home/assets/md/about-right.md'
    about = dict(left=left, right=right)
    heros = []
    for i in range(3):
        msg = f'/home/assets/md/hero-msg-{i+1}.md'
        img = f'/home/assets/img/hero-bg-{i+1}.jpg'
        heros.append(dict(msg=msg, img=img))
    events = qry.get_events(db.session, level=0)
    features = assets.read_json('json/features.json')
    stats = assets.read_json('json/stats.json')
    return render_template('home.html', 
                           about=about,
                           speech=speech,
                           heros=heros,
                           stats=stats,
                           events=events,
                           features=features)

