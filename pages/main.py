
from core.config import app
from .home.routes import bp as home_bp
from .admission.routes import bp as admission_bp
from .courses.routes import bp as courses_bp
from .events.routes import bp as events_bp
from .organisation.routes import bp as org_bp
from .project_a.routes import bp as proj_a_bp
from .project_b.routes import bp as proj_b_bp

app.register_blueprint(home_bp)
app.register_blueprint(admission_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(events_bp)
app.register_blueprint(org_bp)
app.register_blueprint(proj_a_bp)
app.register_blueprint(proj_b_bp)

