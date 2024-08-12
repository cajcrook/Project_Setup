import pytest
from lib.grammer_stats import GrammarStats

"""
ring is inputted.
Return if valid return string, else raise False
"""
def test_valid_string_return_true():
    grammer_stats = GrammarStats()
    grammer_stats.add_text("Hello, it's friday!")
    assert grammer_stats.check() == True

"""
Check a invalid string is inputted - no puncutation at end.
Return False
"""
def test_invalid_string_no_end_punctuation():
    grammer_stats = GrammarStats()
    grammer_stats.add_text("Hello, it's friday")
    assert grammer_stats.check() == False

"""
Check a invalid string is inputted - no capital letter at beginning.
Return False
"""
def test_invalid_string_no_start_capital_letter():
    grammer_stats = GrammarStats()
    grammer_stats.add_text("hello, it's friday!")
    assert grammer_stats.check() == False

"""
Check a invalid string is inputted - no capital letter at beginning or punctuation at end.
Return False
"""
def test_invalid_string_no_start_capital_letter_or_punctuation():
    grammer_stats = GrammarStats()
    grammer_stats.add_text("hello, it's friday")
    assert grammer_stats.check() == False


# """
# Check for empty string
# Return Error Message if empty
# """
# def test_string_is_empty_raise_error():
#     with pytest.raises(Exception) as err:
#         GrammerStats("")
#     assert str(err.value) == "Grammer test requires valid string"
    
"""
Check to see how much of the text has passed/ is good based on Check criteria.
Returns int 50
"""
def test_to_check_how_many_texts_have_been_approved():
    grammer_stats = GrammarStats()
    grammer_stats.add_text("Hello, it's friday!")
    assert grammer_stats.percentage_good() == 100

   
"""
Check to see how much of the text has passed/ is good based on Check criteria.
Returns int 25
"""
def test_to_check_how_many_texts_have_been_approved():
    grammer_stats = GrammarStats()
    grammer_stats.add_text("Hello, it's friday")
    grammer_stats.add_text("Hello, it's friday")
    grammer_stats.add_text("Hello, it's friday")
    grammer_stats.add_text("Hello, it's friday!")
    assert grammer_stats.percentage_good() == 25
    
