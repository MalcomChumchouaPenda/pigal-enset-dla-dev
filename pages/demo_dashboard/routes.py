
import os
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l
from flask import render_template, request, url_for, redirect
from core.utils import (
    UiBlueprint, 
    read_json, 
    read_markdown, 
    paginate_items, 
    default_deadline,
    get_locale
)


ui = UiBlueprint(__name__)
static_dir = os.path.join(os.path.dirname(__file__), 'static')


@ui.route('/charts')
@ui.roles_accepted('developper')
def charts():
    return render_template('demo-dashboard-charts.jinja')

@ui.route('/tables')
@ui.roles_accepted('developper')
def tables():
    persons = [
        {'name':'Brandon Jacob', 'position':'Designer', 'age':28, 'start_date':'2016-05-25'},
        {'name':'Bridie Kessler', 'position':'Developper', 'age':35, 'start_date':'2014-12-05'},
        {'name':'Ashleigh Langosh', 'position':'Finance', 'age':45, 'start_date':'2011-08-12'},
        {'name':'Angus Grady', 'position':'HR', 'age':34, 'start_date':'2012-06-11'},
        {'name':'Raheem Lehner', 'position':'Designer', 'age':47, 'start_date':'2011-04-19'},
    ]
    return render_template('demo-dashboard-tables.jinja', persons=persons)

@ui.route('/datatables')
@ui.roles_accepted('developper')
def datatables():
    addrspath = os.path.join(static_dir, 'json/addresses.json')
    return render_template('demo-dashboard-datatables.jinja', addresses=read_json(addrspath))


@ui.route('/form-editors')
@ui.roles_accepted('developper')
def form_editors():
    return render_template('demo-dashboard-form-editors.jinja')


@ui.route('/form-elements')
@ui.roles_accepted('developper')
def form_elements():
    return render_template('demo-dashboard-form-elements.jinja')


@ui.route('/form-layouts')
@ui.roles_accepted('developper')
def form_layouts():
    return render_template('demo-dashboard-form-layouts.jinja')


@ui.route('/form-validation')
@ui.roles_accepted('developper')
def form_validation():
    return render_template('demo-dashboard-form-validation.jinja')

