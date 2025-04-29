"""
This script defines a function to count the frequency of each word in a given paragraph.

Features:
----------
- Removes punctuation using regular expressions.
- Converts all words to lowercase for case-insensitive counting.
- Uses a dictionary to count and store word occurrences.
- Demonstrates usage with a multi-line paragraph example.

Example:
    Input: "This is a test. This is only a test."
    Output:
        this: 2
        is: 2
        a: 2
        test: 2
        only: 1
"""

import re  # Regular expressions module for extracting words

###############################################################
def count_word_frequency(paragraph):
    """
    Count the frequency of each word in the input paragraph.

    Args:
        paragraph (str): A block of text.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    # Use regex to extract words, ignoring punctuation and case
    words = re.findall(r'\b\w+\b', paragraph.lower())

    # Initialize an empty dictionary to store word frequencies
    word_counts = {}

    # Loop through each word and count its occurrences
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  # Increment count if word already exists
        else:
            word_counts[word] = 1   # Initialize count for a new word

    return word_counts

# -------------------------------------------------------------
# Example usage
# -------------------------------------------------------------
paragraph = """
This is a simple paragraph that is meant to be used for counting the frequency of each word.
This paragraph has some repeated words, and it will be interesting to see the counts.
This is line one
This is line two
That is line thres
"""

# Call the function and print word frequencies
word_frequencies = count_word_frequency(paragraph)
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
