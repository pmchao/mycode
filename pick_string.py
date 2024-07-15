"""
# This script defines a function that takes a list of items and returns a single unified string
# composed of all the string elements in the list concatenated together. If the list contains
# non-string elements, they are ignored.
"""

####################################################################################
def concatenate_strings(a_list):
    # Initialize an empty string to hold the result
    result = ""
    # Iterate through the list
    for item in a_list:
        # Check if the item is a string
        if isinstance(item, str):
            # Concatenate the string item to the result
            result += item
    return result

# Example list
a_list = [1, "H", 3, "ello"]

# Get the unified string
unified_string = concatenate_strings(a_list)

print(f"The unified string is: {unified_string}")
