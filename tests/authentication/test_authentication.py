import pytest
import allure
from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema, \
    RefreshResponseSchema
from fixtures.authentication import AuthenticationFixture
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response, assert_refresh_token_response, \
    assert_refresh_access_token
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from allure_commons.types import Severity


@allure.epic(AllureEpic.LMS)
@allure.suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureFeature.AUTHENTICATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHENTICATION)
@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.title("Login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response, 200)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.sub_suite(AllureStory.VALIDATE_ENTITY)
    @allure.title("Updating an access token using a refresh token")
    @allure.severity(Severity.CRITICAL)
    def test_refresh_token(
            self,
            authentication_client: AuthenticationClient,
            function_authentication: AuthenticationFixture
    ):
        request = RefreshRequestSchema(refresh_token=function_authentication.refresh_token)
        response = authentication_client.refresh_api(request)
        response_data = RefreshResponseSchema.model_validate_json(response.text)

        assert_status_code(response, 200)
        assert_refresh_token_response(request, response_data)
        assert_refresh_access_token(function_authentication.access_token, response_data.token.access_token)

        validate_json_schema(response.json(), response_data.model_json_schema())