import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestShema, CreateExerciseResponseShema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestShema
    response: CreateExerciseResponseShema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercises(
        exercises_client: ExercisesClient,
        function_user: UserFixture,
        function_course: CourseFixture
) -> ExercisesFixture:
    request = CreateExerciseRequestShema(course_id=function_course.response.course.id)
    response = exercises_client.create_exercises(request)
    return ExercisesFixture(request=request, response=response)
