
import pytest
from core.config import db
from plugins.services.demo_v0_0.models import Course


@pytest.fixture
def courses_demo(app):    
    course1 = Course(id="ECO3", title="Economie 3")
    course2 = Course(id="ECO4", title="Economie 4")
    course3 = Course(id="INFO5", title="Informatique 5")    
    db.session.add_all([course1, course2, course3])
    db.session.commit()


def test_create_course(client):
    data = {"id":"MATH1", "title": "Mathematics 1"}
    response = client.post("/api/demo/v0.0/courses", json=data)
    assert response.status_code == 201
    assert "course added" in response.json["message"]

    # Check it's really created
    course = Course.query.filter_by(id="MATH1").first()
    assert course is not None


def test_get_all_courses(client, courses_demo):
    response = client.get("/api/demo/v0.0/courses")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 3


def test_get_single_course(client, courses_demo):
    course_id = 'ECO3'
    response = client.get(f"/api/demo/v0.0/courses/{course_id}")
    assert response.status_code == 200
    assert response.json["title"] == "Economie 3"


def test_get_not_found_course(client, courses_demo):
    course_id = 'ECO6'
    response = client.get(f"/api/demo/v0.0/courses/{course_id}")
    assert response.status_code == 404
    assert "course not found" in response.json["message"]


def test_update_course(client, courses_demo):
    course_id = 'ECO4'
    update_data = {"title": "Modern Economics"}
    response = client.put(f"/api/demo/v0.0/courses/{course_id}", json=update_data)
    assert response.status_code == 200
    assert "course updated" in response.json["message"]

    # Check it's really updated
    course = Course.query.filter_by(id="ECO4").first()
    assert course.title == "Modern Economics"
    

def test_update_course_not_found(client, courses_demo):
    course_id = 'ECO6'
    update_data = {"title": "Modern Economics"}
    response = client.put(f"/api/demo/v0.0/courses/{course_id}", json=update_data)
    assert response.status_code == 404
    assert "course not found" in response.json["message"]


def test_delete_course(client, courses_demo):
    course_id = 'INFO5'
    response = client.delete(f"/api/demo/v0.0/courses/{course_id}")
    assert response.status_code == 204

    # Check it's really updated
    course = Course.query.filter_by(id="INFO5").first()
    assert course is None


def test_delete_course_not_found(client, courses_demo):
    course_id = 'INFO6'
    response = client.delete(f"/api/demo/v0.0/courses/{course_id}")
    assert response.status_code == 404
