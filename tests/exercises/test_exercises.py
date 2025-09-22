import pytest
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestShema, CreateExerciseResponseShema, \
    GetExerciseResponseShema, UpdateExerciseRequestShema, UpdateExerciseResponseShema, GetExercisesResponseShema, \
    GetExercisesQuerySchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExercisesFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercises_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercises(self, function_course: CourseFixture, exercises_client: ExercisesClient):
        request = CreateExerciseRequestShema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseShema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_create_exercises_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(self, function_exercises: ExercisesFixture, exercises_client: ExercisesClient):
        response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        response_data = GetExerciseResponseShema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_get_exercise_response(function_exercises.response.exercise, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercises: ExercisesFixture):
        request = UpdateExerciseRequestShema()
        response = exercises_client.update_exercise_api(
            exercise_id=function_exercises.response.exercise.id,
            request=request
        )
        response_data = UpdateExerciseResponseShema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercises: ExercisesFixture):
        delete_response = exercises_client.delete_exercise_api(function_exercises.response.exercise.id)
        assert_status_code(delete_response.status_code, 200)

        get_response = exercises_client.get_exercise_api(function_exercises.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, 404)
        assert_exercise_not_found_response(get_response_data)

        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_exercises: ExercisesFixture,
            function_course: CourseFixture
    ):
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query)
        response_data = GetExercisesResponseShema.model_validate_json(response.text)

        assert_status_code(response.status_code, 200)
        assert_get_exercises_response([function_exercises.response], response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
