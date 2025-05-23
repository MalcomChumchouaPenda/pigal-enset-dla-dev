
from flask_babel import lazy_gettext as _l
from core.utils import sidebar


# submenu3.add('sub_menu_3_1', _l('Dashboard (avec composants)'), endpoint='demo_dashboard.dashboard', rank=0)
# submenu3.add('sub_menu_3_2', _l('Dashboard (protege)'), endpoint='demo_dashboard.protected', rank=1)
# submenu3.add('sub_menu_3_3', _l('Dashboard (etudiants)'), endpoint='demo_dashboard.student', rank=2)

formmenu = sidebar.add('form_menu', _l('Forms'))
formmenu.add('form_editors_pg', _l('Form editors'), endpoint='demo_dashboard.form_editors')
formmenu.add('form_elements_pg', _l('Form elements'), endpoint='demo_dashboard.form_elements')
formmenu.add('form_layouts_pg', _l('Form layouts'), endpoint='demo_dashboard.form_layouts')
formmenu.add('form_validation_pg', _l('Form validation'), endpoint='demo_dashboard.form_validation')

datamenu = sidebar.add('data_menu', _l('Data'))
datamenu.add('tables_pg', _l('General tables'), endpoint='demo_dashboard.tables')
datamenu.add('datatables_pg', _l('Data tables'), endpoint='demo_dashboard.datatables')
datamenu.add('charts_pg', _l('Data charts'), endpoint='demo_dashboard.charts')
