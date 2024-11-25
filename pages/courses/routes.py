
from flask import render_template
from core.utils import create_ui
from services.demo import queries as qry


ui = create_ui('courses')

@ui.route('/')
def index():
    # data1 = qry.get_courses()
    # data2 = data1[:5]
    # data3 = data1[:4]
    # data4 = data1[:3]
    summary = qry.get_course_types()
    fi = qry.get_formations_by_department('FI')
    cps = qry.get_formations_by_department('CPS')
    m2r = qry.get_formations_by_lab()
    return render_template('courses.html', 
                           summary=summary, 
                           fi=fi, cps=cps, m2r=m2r)