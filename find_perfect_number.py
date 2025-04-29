"""
perfect_number_checker.py

This script checks whether a given positive integer is a *perfect number*.

Definition:
-------------
A perfect number is a positive integer that is equal to the sum of its
proper positive divisors, excluding the number itself.

For example:
- 6 is a perfect number because its divisors are 1, 2, and 3.
  And 1 + 2 + 3 = 6
- 28 is a perfect number because 1 + 2 + 4 + 7 + 14 = 28

Usage:
-------------
Run this script and input a positive integer when prompted.
The program will tell you whether it's a perfect number.

Author: Peter Chao (you can change this to your name)
"""

def is_perfect_number(n):
    """
    Determines if the given number is a perfect number.

    Parameters:
        n (int): The number to check (should be greater than 1)

    Returns:
        bool: True if n is a perfect number, False otherwise
    """
    if n <= 1:
        return False

    divisor_sum = 1  # 1 is a divisor of all numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i

    return divisor_sum == n


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number < 1:
            raise ValueError("Number must be a positive integer.")

        if is_perfect_number(number):
            print(f"{number} is a perfect number!")
        else:
            print(f"{number} is NOT a perfect number.")

    except ValueError as e:
        print(f"Invalid input: {e}")
