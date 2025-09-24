import allure
from clients.authentication.authentication_schema import LoginResponseSchema, RefreshResponseSchema, \
    RefreshRequestSchema
from tools.assertions.base import assert_equal, assert_is_true, assert_unequal
from tools.logger import get_logger


logger = get_logger("AUTHENTICATIONS_ASSERTIONS")


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    logger.info("Check login response")

    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, "access_token")
    assert_is_true(response.token.refresh_token, "refresh_token")

@allure.step("Check refresh token response")
def assert_refresh_token_response(request: RefreshRequestSchema, response: RefreshResponseSchema):
    logger.info("Check refresh token response")

    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, "access_token")
    assert_equal(response.token.refresh_token, request.refresh_token, "refresh_token")

@allure.step("Check that old access token does not match the new access token")
def assert_refresh_access_token(old_access_token: str, new_access_token: str):
    logger.info("Check that old access token does not match the new access token")

    assert_unequal(old_access_token, new_access_token, "access_token")
