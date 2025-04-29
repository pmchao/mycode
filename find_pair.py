"""
This script defines a function to find all unique pairs of numbers in a list
that add up to a given target sum. Each number can only be used once.

For example:
Input  : numbers = [2, 5, 5, 5, 4, 3, 7, 8], target = 10
Output : [(5, 5), (7, 3)]
"""

def find_pairs_with_sum(numbers, target):
    """
    Find all unique pairs in the list that sum up to the given target.

    Args:
        numbers (list of int): The list of integers to search.
        target (int): The target sum for the pairs.

    Returns:
        list of tuple: A list of tuples, each representing a valid pair.
    """
    seen = set()   # Tracks numbers we've already seen
    pairs = []     # Stores the resulting pairs

    for number in numbers:
        complement = target - number
        if complement in seen:
            # Valid pair found — add to result
            pairs.append((number, complement))

            # Remove complement to avoid reusing the same number
            seen.remove(complement)
        else:
            # Save number for future pair checking
            seen.add(number)

    return pairs

# Example usage
numbers = [2, 5, 5, 5, 4, 3, 7, 8]
target = 10
print(find_pairs_with_sum(numbers, target))
