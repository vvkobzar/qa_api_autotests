import allure
from typing import Any, Sized
from httpx import Response


@allure.step("Check that response status code equals to {expected_status_code}")
def assert_status_code(response: Response, expected_status_code: int):
    assert  response.status_code == expected_status_code, (
        "Incorrect response status code. "
        f"Expected status code: {expected_status_code}. "
        f"Response status code: {response.status_code}"
    )


@allure.step("Check that {name} equals to {expected}")
def assert_equal(expected: Any, actual: Any, name: str):
    assert expected == actual, (
       f"Incorrect value: '{name}', "
       f"Expected value: '{expected}' "
       f"Actual value: '{actual}'"
    )

@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(expected: Sized, actual: Sized, name: str):
    with allure.step(f"Check that length of {name}, equals to {len(expected)}"):
        assert len(expected) == len(actual), (
            f"Incorrect object length: '{name}'. "
            f"Expected length: {len(expected)}. "
            f"Actual length: {len(actual)}. "
        )
