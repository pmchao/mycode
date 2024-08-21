

"""
Find pair with target sum
"""


def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = []
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.append((number, complement))
        seen.add(number)
    return pairs

# Example usage
numbers = [2, 4, 3, 5, 7, 8, 1]
target = 10
print(find_pairs_with_sum(numbers, target))
