
from flask import request, abort
from flask_restx import Resource, fields
from core.utils import ApiNamespace
from core.config import db
from .models import Course


ns = ApiNamespace('demo', description="Demo services")

course = ns.model('Course', {
    'id': fields.String(required=True, description="Course identifier"),
    'title': fields.String(required=True, description='Title of courses')
})


@ns.route('/courses')
class CoursesApi(Resource):

    @ns.marshal_list_with(course)
    @ns.doc('get_all_courses')
    def get(self):
        return Course.query.all()

    @ns.doc('create_one_courses')
    def post(self):
        data = request.get_json()
        course = Course(id=data['id'], title=data["title"])
        db.session.add(course)
        db.session.commit()
        return {"message": "course added"}, 201


@ns.route('/courses/<id>')
class CourseApi(Resource):

    @ns.marshal_with(course)
    @ns.doc('get_one_course')
    def get(self, id):
        course = Course.query.filter_by(id=id).first()
        if not course:
            return abort(404, "course not found")
        return course

    @ns.doc('update_one_course')
    def put(self, id):
        course = Course.query.filter_by(id=id).first()
        if not course:
            return {"message": "course not found"}, 404
        data = request.get_json()
        course.title = data.get("title", course.title)
        db.session.commit()
        return {"message": "course updated"}, 200

    @ns.doc('delete_one_course')
    def delete(self, id):
        course = Course.query.filter_by(id=id).first()
        if not course:
            return "", 404
        db.session.delete(course)
        db.session.commit()
        return "", 204
