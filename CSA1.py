import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    pattern = r'\b[A-Z][a-z]*\b'
    names = re.findall(pattern,simple_string)
    return (names)
    raise NotImplementedError()


assert len(names()) == 4, "There are four names in the simple_string"