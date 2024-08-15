def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(str.isalnum, s)).lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Example usage
#input_string = input("Enter a string: ")
input_string = 'abba'
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

######################################################

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(filter(str.isalnum, s)).lower()

    # Use two pointers to check for palindrome
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is NOT a palindrome.')
