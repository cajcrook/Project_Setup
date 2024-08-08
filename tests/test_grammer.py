

from lib.grammer import check_grammer  

"""
Input string with capital letter at beginning and ! at the end.
Returns True.
"""
def test_both_capital_and_exclamation_mark():
    result = check_grammer("Hello everyone!")
    assert result == True
    

"""
Input string with capital letter at beginning and NO punctuation at the end.
Returns False.
"""
def test_with_capital_letter_no_punctuation():
    result = check_grammer("Hello everyone")
    assert result == False


"""
Input string with capital letter at beginning and ? at the end.
Returns True.
"""
def test_both_capital_and_question_mark():
    result = check_grammer("Hello everyone?")
    assert result == True


"""
Input string with capital letter at beginning and . at the end.
Returns True.
"""
def test_both_capital_and_full_stop():
    result = check_grammer("Hello everyone.")
    assert result == True


"""
Input string with NO capital letter at beginning but has punctuation at the end.
Returns False.
"""
def test_no_capital_but_has_full_stop():
    result = check_grammer("hello everyone.")
    assert result == False


"""
Input string with NO capital letter at beginning and NO punctuation at the end.
Returns False.
"""
def test_no_capital_and_no_punctuation():
    result = check_grammer("hello everyone")
    assert result == False


# """
# Input empty string
# Return error message
# """
# def test_empty_string_return_error_message():
#     result = check_grammer("")
#     with pytest.raises(Exception) as err:
#         check_grammer()
#     error_message = str(err.value)  
#     assert error_message == "No input"
    


"""
Input two sentence string with valid criteria
Returns True

def test__two_sentences_with_valid_criteria():
    result = check_grammer("Hello everyone. is it me?")
    assert result == True
"""
# refactor code
