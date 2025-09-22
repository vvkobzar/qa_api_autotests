import allure
from clients.api_clients import APIClient
from httpx import Response
from clients.authentication.authentication_schema import RefreshRequestSchema, LoginRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def get_login_response(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
