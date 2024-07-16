"""
This function finds the second smallest unique number in a list of integers.
It raises a ValueError if the list contains fewer than two numbers or if there
are not at least two unique numbers in the list.

Example usage:
numbers = [5, 1, 8, 3, 1, 5, 8, 3]
print(second_min(numbers))  # Output: 3
"""
#####################################################################
def second_min(numbers):
    # Check if the list contains at least two numbers
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")

    # Initialize the two smallest numbers to positive infinity
    min1 = float('inf')
    min2 = float('inf')

    # Iterate through the list to find the two smallest unique numbers
    for num in numbers:
        if num < min1:
            min2, min1 = min1, num  # Update both min1 and min2
        elif min1 < num < min2:
            min2 = num  # Update only min2

    # Check if there are at least two unique numbers
    if min2 == float('inf'):
        raise ValueError("List must contain at least two unique numbers.")

    return min2  # Return the second smallest number

# Example usage
numbers = [5, 1, 8, 3, 2,1, 5, 8, 3]
print(second_min(numbers))  # Output: 3
