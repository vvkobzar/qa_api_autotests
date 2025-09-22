import allure
from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from tools.assertions.base import assert_equal
from clients.files.files_schema import FileSchema
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response


@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(expected_url, str(response.file.url), "url")
    assert_equal(request.filename, response.file.filename, "file_name")
    assert_equal(request.directory, response.file.directory, "directory")

@allure.step("Check file")
def assert_file(expected: FileSchema, actual: FileSchema):
    assert_equal(expected.id, actual.id, "id")
    assert_equal(expected.url, actual.url, "url")
    assert_equal(expected.filename, actual.filename, "file_name")
    assert_equal(expected.directory, actual.directory, "directory")

@allure.step("Check get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    assert_file(create_file_response.file, get_file_response.file)

@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(expected, actual)

@allure.step("Check create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(expected, actual)

@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(detail="File not found")
    assert_internal_error_response(expected, actual)

@allure.step("Check get file with incorrect file id response")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` "
                             "followed by [0-9a-fA-F-], found `i` at 1"
                },
                message="Input should be a valid UUID, invalid character: "
                        "expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(expected, actual)
