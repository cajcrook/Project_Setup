from lib.count_words import count_words

"""
A function called count_words that takes a string
as an argument
and returns the number of words in that string.
"""

"""
tests empty string
returns empty string
"""
def test_string_is_empty():
    result = count_words("")
    assert result == 1

"""
tests string with five words
returns number of words in string
"""
def test_string_with_5_words():
    result = count_words("One two three four five")
    assert result == 5
