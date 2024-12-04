
from flask import render_template
from core.utils import create_ui, get_assets


ui = create_ui('home')
assets = get_assets('home')
event_assets = get_assets('events')



@ui.route('/')
@ui.route('/login')
def index():
    about = _load_about()
    heros = _load_heros()
    speech = _load_speech()
    events = _load_events()
    features = _load_features()
    return render_template('home.html', 
                           about=about,
                           heros=heros,
                           speech=speech,
                           events=events,
                           features=features)

def _load_heros():
    heros = []
    for i in range(3):
        msg = assets.read_markdown(f'md/hero-msg-{i+1}.md')
        img = f'img/hero-bg-{i+1}.jpg'
        heros.append(dict(msg=msg, img=img))
    return heros

def _load_speech():
    return assets.read_markdown(f'md/speech.md')

def _load_about():
    left = assets.read_markdown(f'md/about-left.md')
    right = assets.read_markdown(f'md/about-right.md')
    return dict(left=left, right=right)

def _load_features():
    return assets.read_json(f'json/features.json')

def _load_events():
    events = event_assets.read_json('json/events.json')
    recent = []
    for item in events:
        if item['level'] == 0:
            item_id = item["id"]
            item['text'] = event_assets.read_markdown(f'md/{item_id}-100.md')
            recent.append(item)
    return recent
