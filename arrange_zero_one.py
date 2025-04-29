"""
Reorganize a list such that:
- All 0s are moved to the beginning (left)
- All 1s are moved to the end (right)
- All other numbers stay in the middle, preserving their original order

Example:
Input : [1, 2, 3, 1, 0, 4, 5, 0]
Output: [0, 0, 2, 3, 4, 5, 1, 1]
"""

# Original list
my_list = [1, 2, 3, 1, 0, 4, 5, 0]

# Reorganize the list as described above
processed_list = (
    [x for x in my_list if x == 0] +                # Zeros to the front
    [x for x in my_list if x not in (0, 1)] +       # All others in the middle
    [x for x in my_list if x == 1]                  # Ones to the end
)

# Display results
print("Original list:", my_list)
print("Processed list:", processed_list)

