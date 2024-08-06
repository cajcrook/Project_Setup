from lib.make_snippet import make_snippet

"""
tests empty string 
return empty string
"""
def test_empty_string():
    result = make_snippet("")
    assert result == ""

"""
test string of 4 words
returns 4 words
"""
def test_four_word_string():
    result = make_snippet("One two three four")
    assert result == "One two three four"

"""
test string of 5 words
returns 5 words
"""
def test_five_word_string():
    result = make_snippet("One two three four five")
    assert result == "One two three four five"

"""
test string of 6 words
returns 5 words and ...
"""
def test_six_word_string():
    result = make_snippet("One two three four five six")
    assert result == "One two three four five..."




