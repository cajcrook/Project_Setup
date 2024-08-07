from lib.reading_time import reading_time

"""
Input empty string
Return 0
"""
def test_input_0_word_str_returns_0():
    result = reading_time("")
    assert result == 0


"""
Input is simple string of 100 word
It returns a est. time of 0.5 of a minute
"""
def test_input_100_word_str_returns_05():
    result = reading_time("One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten")
    assert result == 0.5

"""
Input 200 word string
return est time of 1 minute
"""
def test_input_200_word_str_returns_1():
    result = reading_time("One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten")
    assert result == 1

"""
Input 212 word string
Return est time of 
"""
def test_input_212_word_str_returns_1():
    result = reading_time("One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two three four five six seven eight nine ten One two")
    assert result == 1.06
