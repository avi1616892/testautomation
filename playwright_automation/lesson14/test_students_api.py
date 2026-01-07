import json

import pytest
from playwright.sync_api import Playwright

WEATHER_API_URL="http://localhost:9000/student/"
HEADERS={'content-type':'application/json'}
STUDENT_ID='100'
class Test_Open_Weather_Map:
    @pytest.fixture(scope='class',autouse=True)
    def setup(self,playwright:Playwright):
        global  request_context
        request_context=playwright.request.new_context(base_url=WEATHER_API_URL,extra_http_headers=HEADERS)
        yield
        request_context.dispose()

    def test_get_students(self):
        response=request_context.get(url="list")
        student_list=response.json()
        print("\nStudent")
        for student in student_list:
            print(f"{student["id"]} - {student["firstName"]}  {student["lastName"]}")
        assert response.status == 200

    def test_post_students(self):
        my_courses=["Python Course","CSharp Course","Java Course"]
        students_data={"firstName": "Avi","lastName": "Gavrilov","email": "avi@massaQuisqueporttitor.org","programme": "It","courses": my_courses}
        response = request_context.post(url="",data=students_data)
        created_student=response.json()
        print(json.dumps(created_student,indent=2))
        assert response.status == 201

    def test_put_students(self):
        my_courses=["Python Course","CSharp Course","Java Course"]
        updated_students_data={"firstName": "Avi","lastName": "Gavrilov","email": "avi@massaQuisqueporttitor.org","programme": "QA Automation","courses": my_courses}
        response = request_context.put(url=STUDENT_ID,data=updated_students_data)
        update_student=response.json()
        print(json.dumps(update_student,indent=2))
        assert response.status == 200

    def test_delete_students(self):
        response = request_context.delete(url=STUDENT_ID)
        print(response)
        assert response.status == 204


