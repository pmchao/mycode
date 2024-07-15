import re

"""
This function takes a string as input, extracts all numerical values (both integers and floating-point numbers)
using a regular expression, converts them to floats, and returns their sum.
"""
################################################################################################
def sum_of_numbers_in_string(s):
    # Regular expression to match integers and floats, including those embedded in words
    #numbers = re.findall(r'\d+\.?\d*|\.\d+', s)
    numbers = re.findall(r'-?\d+\.?\d*|\-\.\d+|\.\d+', s)
    # Convert the extracted numbers to floats and sum them
    total_sum = sum(map(float, numbers))
    return total_sum

# Example string
string = "Some text with numbers like 4,5 and -6, floats like 4.5 and 6.7 and mixed like Python3"

# Calculate the sum
result = sum_of_numbers_in_string(string)

# Print the result
print(f"The sum of all numerical values in the string is: {result}")
