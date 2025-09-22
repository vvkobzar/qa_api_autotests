import allure
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestShema, CreateExerciseResponseShema, ExerciseShema, \
    GetExerciseResponseShema, UpdateExerciseRequestShema, UpdateExerciseResponseShema, GetExercisesResponseShema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


allure.step("Check create exercises response")
def assert_create_exercises_response(request: CreateExerciseRequestShema, response: CreateExerciseResponseShema):
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

allure.step("Check exercise")
def assert_exercise(expected: ExerciseShema, actual: ExerciseShema):
    assert_equal(expected.id, actual.id, "id")
    assert_equal(expected.title, actual.title, "title")
    assert_equal(expected.course_id, actual.course_id, "course_id")
    assert_equal(expected.max_score, actual.max_score, "max_score")
    assert_equal(expected.min_score, actual.min_score, "min_score")
    assert_equal(expected.order_index, actual.order_index, "order_index")
    assert_equal(expected.description, actual.description, "description")
    assert_equal(expected.estimated_time, actual.estimated_time, "estimated_time")

allure.step("Check get exercise response")
def assert_get_exercise_response(created_exercise, response: GetExerciseResponseShema):
    assert_exercise(created_exercise, response.exercise)

allure.step("Check update exercise response")
def assert_update_exercise_response(request: UpdateExerciseRequestShema, response: UpdateExerciseResponseShema):
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")

allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(expected, actual)

allure.step("Check get exercises response")
def assert_get_exercises_response(
        create_exercises_response: list[CreateExerciseResponseShema],
        get_exercises_response: GetExercisesResponseShema
):
    assert_length(create_exercises_response, get_exercises_response.exercises, "exercises")

    for index, create_exercise_response in enumerate(create_exercises_response):
        assert_exercise(create_exercise_response.exercise, get_exercises_response.exercises[index])
