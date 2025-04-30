"""
This script defines two versions of a function to check if a string is a palindrome.

A palindrome is a word, phrase, or sequence that reads the same forward and backward,
ignoring case and non-alphanumeric characters.

The script:
1. Cleans the input string (removes spaces/punctuation, converts to lowercase).
2. Compares characters using slicing (version 1) or two-pointer technique (version 2).
3. Prints whether the input is a palindrome.

Examples:
- 'abba'       → Palindrome
- 'RaceCar'    → Palindrome
- 'Hello'      → Not a palindrome
- 'A man, a plan, a canal: Panama' → Palindrome
"""

# ----------------------
# Version 1: Simple reverse comparison using slicing
# ----------------------
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(str.isalnum, s)).lower()

    # Check if the cleaned string is equal to its reverse
    return s == s[::-1]

# Example usage
# input_string = input("Enter a string: ")
input_string = 'abba'
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

# =====================================================
# Version 2: Two-pointer method (more explicit logic)
# =====================================================
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(filter(str.isalnum, s)).lower()

    # Use two pointers from both ends to check characters one by one
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage with user input
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is NOT a palindrome.')
