"""
This script provides two functions to convert a decimal number into:
- Binary format (base-2)
- Hexadecimal format (base-16)

It demonstrates how to perform manual conversion using loops and string manipulation
without relying on Python's built-in `bin()` or `hex()` functions.
"""


def decimal_to_binary(n):
    """
    Convert a decimal number to its binary representation.

    Args:
        n (int): The decimal number to convert.

    Returns:
        str: The binary representation of the number as a string.
    """
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  # Append remainder (0 or 1) to the left
        n = n // 2  # Integer division to reduce the number
    return binary


def decimal_to_hex(n):
    """
    Convert a decimal number to its hexadecimal representation.

    Args:
        n (int): The decimal number to convert.

    Returns:
        str: The hexadecimal representation of the number as a string.
    """
    if n == 0:
        return "0"

    hex_digits = "0123456789ABCDEF"  # Lookup table for hex digits
    hex_representation = ""
    while n > 0:
        hex_representation = hex_digits[n % 16] + hex_representation  # Add hex digit
        n = n // 16
    return hex_representation


# Example usage with a hardcoded decimal value
decimal_number = 26

# Convert to binary (uncomment if needed)
# binary_representation = decimal_to_binary(decimal_number)

# Convert to hexadecimal
hex_representation = decimal_to_hex(decimal_number)

# Display results
# print(f"The binary representation of {decimal_number} is {binary_representation}")
print(f"The hexadecimal representation of {decimal_number} is {hex_representation}")
