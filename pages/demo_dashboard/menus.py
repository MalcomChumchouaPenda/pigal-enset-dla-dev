
from flask_babel import lazy_gettext as _l
from core.utils import sidebar


# submenu3.add('sub_menu_3_1', _l('Dashboard (avec composants)'), endpoint='demo_dashboard.dashboard', rank=0)
# submenu3.add('sub_menu_3_2', _l('Dashboard (protege)'), endpoint='demo_dashboard.protected', rank=1)
# submenu3.add('sub_menu_3_3', _l('Dashboard (etudiants)'), endpoint='demo_dashboard.student', rank=2)

formmenu = sidebar.add('form_menu', _l('Forms'), accepted=['developper'])
formmenu.add('form_editors_pg', _l('Form editors'), endpoint='demo_dashboard.form_editors')
formmenu.add('form_elements_pg', _l('Form elements'), endpoint='demo_dashboard.form_elements')
formmenu.add('form_layouts_pg', _l('Form layouts'), endpoint='demo_dashboard.form_layouts')
formmenu.add('form_validation_pg', _l('Form validation'), endpoint='demo_dashboard.form_validation')

tablemenu = sidebar.add('table_menu', _l('Tables'), accepted=['developper'])
tablemenu.add('tables_pg', _l('General tables'), endpoint='demo_dashboard.tables')
tablemenu.add('datatables_pg', _l('Data tables'), endpoint='demo_dashboard.datatables')

chartmenu = sidebar.add('charts_menu', _l('Charts'), accepted=['developper'])
chartmenu.add('charts_pg', _l('Basic charts'), endpoint='demo_dashboard.charts')
chartmenu.add('apexcharts_pg', _l('Apex charts'), endpoint='demo_dashboard.apexcharts')
chartmenu.add('echarts_pg', _l('Echarts'), endpoint='demo_dashboard.echarts')

compmenu = sidebar.add('comp_menu', _l('Components'), accepted=['developper'])
compmenu.add('alerts_pg', _l('Alerts'), endpoint='demo_dashboard.alerts')
compmenu.add('badges_pg', _l('Badges'), endpoint='demo_dashboard.badges')
compmenu.add('buttons_pg', _l('Buttons'), endpoint='demo_dashboard.buttons')
compmenu.add('cards_pg', _l('Cards'), endpoint='demo_dashboard.cards')
compmenu.add('list_group_pg', _l('List group'), endpoint='demo_dashboard.list_group')
compmenu.add('modal_pg', _l('Modal'), endpoint='demo_dashboard.modal')
compmenu.add('pagination_pg', _l('Paginations'), endpoint='demo_dashboard.pagination')
compmenu.add('progress_pg', _l('Progress'), endpoint='demo_dashboard.progress')
compmenu.add('spinners_pg', _l('Spinners'), endpoint='demo_dashboard.spinners')
compmenu.add('tabs_pg', _l('Tabs'), endpoint='demo_dashboard.tabs')
compmenu.add('tooltips_pg', _l('Tooltips'), endpoint='demo_dashboard.tooltips')
