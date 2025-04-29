def find_pairs_with_sum(numbers, target):
    seen = set()
    pairs = []
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.append((number, complement))
            # Remove both numbers from `seen` to avoid reusing them
            seen.remove(complement)
        else:
            seen.add(number)
    return pairs

# Example usage
numbers = [2, 5, 5, 5, 4, 3, 7, 8]
target = 10
print(find_pairs_with_sum(numbers, target))
