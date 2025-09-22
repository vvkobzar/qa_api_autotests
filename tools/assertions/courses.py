import allure
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


@allure.step("Check update course response")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    assert_equal(request.title, response.course.title, "title")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")

@allure.step("Check course")
def assert_course(expected: CourseSchema, actual: CourseSchema):
    assert_equal(expected.id, actual.id, "id")
    assert_equal(expected.title, actual.title, "title")
    assert_equal(expected.max_score, actual.max_score, "max_score")
    assert_equal(expected.min_score, actual.min_score, "min_score")
    assert_equal(expected.description, actual.description, "description")
    assert_equal(expected.estimated_time, actual.estimated_time, "estimated_time")

    assert_file(expected.preview_file, actual.preview_file)
    assert_user(expected.created_by_user, actual.created_by_user)

@allure.step("Check get courses response")
def assert_get_courses_response(
        create_course_responses: list[CreateCourseResponseSchema],
        get_courses_responses: GetCoursesResponseSchema
):
    assert_length(create_course_responses, get_courses_responses.courses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(create_course_response.course, get_courses_responses.courses[index])

@allure.step("Check create course response")
def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    assert_equal(request.title, response.course.title, "title")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")
    assert_equal(request.preview_file_id, response.course.preview_file.id, "preview_file_id")
    assert_equal(request.created_by_user_id, response.course.created_by_user.id, "created_by_user_id")
