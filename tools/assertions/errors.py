from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema, InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length


def assert_validation_error(expected: ValidationErrorSchema, actual: ValidationErrorSchema):
    assert_equal(expected.type, actual.type, "type")
    assert_equal(expected.input, actual.input, "input")
    assert_equal(expected.context, actual.context, "context")
    assert_equal(expected.message, actual.message, "message")
    assert_equal(expected.location, actual.location, "location")

def assert_validation_error_response(
        expected: ValidationErrorResponseSchema,
        actual: ValidationErrorResponseSchema
):
    assert_length(expected.details, actual.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(detail, actual.details[index])

def assert_internal_error_response(
        expected: InternalErrorResponseSchema,
        actual: InternalErrorResponseSchema
):
    assert_equal(expected.details, actual.details, "details")
