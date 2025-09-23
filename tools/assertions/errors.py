import allure
from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger


logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(expected: ValidationErrorSchema, actual: ValidationErrorSchema):
    logger.info("Check validation error")

    assert_equal(expected.type, actual.type, "type")
    assert_equal(expected.input, actual.input, "input")
    assert_equal(expected.context, actual.context, "context")
    assert_equal(expected.message, actual.message, "message")
    assert_equal(expected.location, actual.location, "location")

@allure.step("Check validation error response")
def assert_validation_error_response(
        expected: ValidationErrorResponseSchema,
        actual: ValidationErrorResponseSchema
):
    logger.info("Check validation error response")

    assert_length(expected.details, actual.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(detail, actual.details[index])

@allure.step("Check internal error response")
def assert_internal_error_response(
        expected: InternalErrorResponseSchema,
        actual: InternalErrorResponseSchema
):
    logger.info("Check internal error response")

    assert_equal(expected.details, actual.details, "details")
