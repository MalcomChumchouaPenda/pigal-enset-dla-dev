
from core.config import ma
from .models import Course


class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Course
        load_instance = True

    id = ma.auto_field()
    title = ma.auto_field()

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)
