"""
This script demonstrates how to define and use custom exceptions in Python.

Features:
---------
- Defines a base custom exception class `CustomError`.
- Implements two specific exceptions:
    - `ValueTooSmallError` — raised when a value is below a minimum threshold.
    - `ValueTooLargeError` — raised when a value exceeds a maximum threshold.
- Includes a function `check_value()` to validate input and raise appropriate exceptions.
- Demonstrates usage with multiple test cases using `try`/`except`.

Author: [Your Name]
"""

# Define a base class for all custom exceptions
class CustomError(Exception):
    """Base class for other exceptions"""
    pass

# Exception raised when the input value is too small
class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""

    def __init__(self, message="The value is too small."):
        self.message = message
        super().__init__(self.message)

# Exception raised when the input value is too large
class ValueTooLargeError(CustomError):
    """Raised when the input value is too large"""

    def __init__(self, message="The value is too large."):
        self.message = message
        super().__init__(self.message)

# Function to validate a given value and raise appropriate exceptions
def check_value(value):
    """
    Check if the input value is within the acceptable range (10–100).

    Args:
        value (int): The value to check.

    Raises:
        ValueTooSmallError: If the value is less than 10.
        ValueTooLargeError: If the value is greater than 100.
    """
    if value < 10:
        raise ValueTooSmallError(f"The value {value} is too small.")
    elif value > 100:
        raise ValueTooLargeError(f"The value {value} is too large.")
    else:
        print(f"The value {value} is within the acceptable range.")

# Test cases to demonstrate behavior
if __name__ == "__main__":
    try:
        # Test with a value that is too small
        check_value(5)
    except ValueTooSmallError as e:
        print(e)
    except ValueTooLargeError as e:
        print(e)

    try:
        # Test with a value that is too large
        check_value(150)
    except ValueTooSmallError as e:
        print(e)
    except ValueTooLargeError as e:
        print(e)

    try:
        # Test with a value within the acceptable range
        check_value(50)
    except CustomError as e:
        print(e)
