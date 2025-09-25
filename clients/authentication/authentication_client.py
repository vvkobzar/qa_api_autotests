import allure
from clients.api_clients import APIClient
from httpx import Response
from clients.authentication.authentication_schema import RefreshRequestSchema, LoginRequestSchema, LoginResponseSchema
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes
from clients.api_coverage import tracker


class AuthenticationClient(APIClient):
    @allure.step("Authenticate user")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}/login")
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post(f"{APIRoutes.AUTHENTICATION}/login", json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    @tracker.track_coverage_httpx(f"{APIRoutes.AUTHENTICATION}/refresh")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        return self.post(f"{APIRoutes.AUTHENTICATION}/refresh", json=request.model_dump(by_alias=True))

    def get_login_response(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
