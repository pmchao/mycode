class CustomError(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""

    def __init__(self, message="The value is too small."):
        self.message = message
        super().__init__(self.message)


class ValueTooLargeError(CustomError):
    """Raised when the input value is too large"""

    def __init__(self, message="The value is too large."):
        self.message = message
        super().__init__(self.message)


def check_value(value):
    """Function to check the value and raise custom exceptions."""
    if value < 10:
        raise ValueTooSmallError(f"The value {value} is too small.")
    elif value > 100:
        raise ValueTooLargeError(f"The value {value} is too large.")
    else:
        print(f"The value {value} is within the acceptable range.")


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


    #Try it with a number within value.

    try:
        # Test with a value within the acceptable range
        check_value(50)
    except CustomError as e:
        print(e)
