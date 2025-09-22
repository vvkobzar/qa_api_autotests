import allure
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, "access_token")
    assert_is_true(response.token.refresh_token, "refresh_token")
