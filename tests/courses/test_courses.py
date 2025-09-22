import pytest
import allure
from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesQuerySchema, GetCoursesResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update course")
    @allure.severity(Severity.CRITICAL)
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(function_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_ENTITIES)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("Get courses")
    @allure.severity(Severity.BLOCKER)
    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_course: CourseFixture,
            function_user: UserFixture
    ):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_get_courses_response([function_course.response], response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create course")
    @allure.severity(Severity.BLOCKER)
    def test_create_course(self, courses_client: CoursesClient, function_file: FileFixture, function_user: UserFixture):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id
        )
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_create_course_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
        