from collections import Counter


def anagram_period(s):
    """
    Function to find the anagram period of a given string.
    Anagram period is the smallest length of a substring that, when repeated,
    forms a string that is an anagram of the original string.
    """
    n = len(s)
    for i in range(1, n // 2 + 1):  # Only need to check up to half the length of the string
        if n % i == 0:  # Check if i is a divisor of the length of the string
            is_period = True
            base_substr_counter = Counter(s[:i])
            for j in range(i, n, i):
                if Counter(s[j:j + i]) != base_substr_counter:
                    is_period = False
                    break
            if is_period:
                return i  # i is the anagram period

    return n
#  s = "abccbaacb"
#s = "abccbaacb"
s = "aabb"

res = anagram_period(s)
print(res)