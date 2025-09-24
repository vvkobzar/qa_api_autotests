import pytest
from pydantic import BaseModel
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture


class AuthenticationFixture(BaseModel):
    request: LoginRequestSchema
    response: LoginResponseSchema

    @property
    def refresh_token(self) -> str:
        return self.response.token.refresh_token

    @property
    def access_token(self) -> str:
        return self.response.token.access_token

@pytest.fixture
def authentication_client() -> AuthenticationClient:
    return get_authentication_client()


@pytest.fixture
def function_authentication(
        function_user: UserFixture,
        authentication_client: AuthenticationClient,
) -> AuthenticationFixture:
    request = LoginRequestSchema(email=function_user.email, password=function_user.password)
    response = authentication_client.get_login_response(request)
    return AuthenticationFixture(request=request, response=response)
