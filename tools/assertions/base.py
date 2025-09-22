from typing import Any, Sized


def assert_status_code(actual: int, expected: int):
    assert expected == actual, (
        "Incorrect response status code. "
        f"Expected status code: {expected}. "
        f"Actual status code: {actual}"
    )


def assert_equal(expected: Any, actual: Any, name: str):
    assert expected == actual, (
       f"Incorrect value: '{name}', "
       f"Expected value: '{expected}' "
       f"Actual value: '{actual}'"
    )

def assert_is_true(actual: Any, name: str):
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )

def assert_length(expected: Sized, actual: Sized, name: str):
    assert len(expected) == len(actual), (
        f"Incorrect object length: '{name}'. "
        f"Expected length: {len(expected)}. "
        f"Actual length: {len(actual)}. "
    )
