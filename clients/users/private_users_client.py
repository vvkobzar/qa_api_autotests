import allure
from httpx import Response
from clients.api_clients import APIClient
from clients.private_httpx_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import GetUserResponseSchema, UpdateUserRequestSchema
from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    @allure.step("Get user me")
    def get_user_me_api(self) -> Response:
        return self.get(f"{APIRoutes.USERS}/me")

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        return self.patch(f"{APIRoutes.USERS}/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"{APIRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        resource = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(resource.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))