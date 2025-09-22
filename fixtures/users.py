import pytest
from pydantic import BaseModel, EmailStr
from clients.private_httpx_builder import AuthenticationUserSchema
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.public_users_client import PublicUsersClient
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return  AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def private_user_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)
