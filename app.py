
import os
import click
import markdown as md
from flask import redirect, url_for, request, session
from core.utils import read_markdown
from core.config import create_app


app = create_app()


# CLASSIC ROUTES

@app.route('/')
def index():
    return redirect(url_for('home.index'))

@app.route('/change_lang')
def change_lang():
    next = request.referrer
    if not next:
        next = url_for('home.index')
    lang = request.args.get('lang', 'fr')
    session['lang'] = lang
    return redirect(next)


# JINJA FILTERS

@app.template_filter('md')
def convert_to_safe(text, default=None):
    return md.markdown(text)

@app.template_filter('safe_md')
def convert_to_safe(filename, default=None):
    safe = app.jinja_env.filters['safe']
    try:
        return safe(read_markdown(filename))
    except FileNotFoundError:
        if default is not None:
            return safe(default)
        raise


# CLI COMMANDS

@app.cli.group()
def translate():
    """Translation and localization commands."""

@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d translations'):
        raise RuntimeError('compile command failed')

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i messages.pot -d translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')


@app.cli.group()
def demo():
    """Demo management."""

@demo.command()
def clear():
    """Clear all demo databases"""


if __name__=='__main__':
    app.run(debug=True)
    