import re

###############################################################
def count_word_frequency(paragraph):
    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', paragraph.lower())

    # Initialize an empty dictionary to count word frequencies
    word_counts = {}

    # Count the frequency of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
# Example usage
#"""
paragraph = """
This is a simple paragraph that is meant to be used for counting the frequency of each word.
This paragraph has some repeated words, and it will be interesting to see the counts.
This is line one
This is line two
That is line thres
"""

word_frequencies = count_word_frequency(paragraph)
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
