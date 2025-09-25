import allure
from httpx import Response
from clients.api_clients import APIClient
from clients.exercises.exercises_schema import CreateExerciseRequestShema, CreateExerciseResponseShema, \
    UpdateExerciseRequestShema, GetExercisesQuerySchema
from clients.private_httpx_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes
from clients.api_coverage import tracker


class ExercisesClient(APIClient):
    @allure.step("Get exercises")
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def get_exercises_api(self, course_id: GetExercisesQuerySchema) -> Response:
        return self.get(APIRoutes.EXERCISES, params=course_id.model_dump(by_alias=True))

    @allure.step("Create exercise")
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def create_exercise_api(self, request: CreateExerciseRequestShema) -> Response:
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise_api(self, exercise_id) -> Response:
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")

    @allure.step("Update exercise by id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise_api(self, exercise_id, request: UpdateExerciseRequestShema) -> Response:
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def delete_exercise_api(self, exercise_id):
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    def create_exercises(self, request: CreateExerciseRequestShema) -> CreateExerciseResponseShema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseShema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
