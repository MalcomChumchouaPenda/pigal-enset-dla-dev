
from flask import render_template
from core.utils import create_ui, get_assets


ui = create_ui('research')
assets = get_assets('research')


@ui.route('/')
def index():
    return render_template('research.html',
                           hero_msg=_load_hero_msg())

def _load_hero_msg():
    return assets.read_markdown(f'md/hero-msg.md')
