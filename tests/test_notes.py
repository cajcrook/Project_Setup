from lib.notes import check_notes

""""
Input - string including #TODO eg "I've a task #TODO"
Output - True
"""
def test_return_true_if_valid():
    result = check_notes("I've a task #TODO")
    assert result == True

""""
Input - string excluding #TODO eg "I've a task"
Output - False
"""
def test_return_false_if_invalid():
    result = check_notes("I've a task")
    assert result == False

"""
Check data type eg. 101.1
Return Not valid if not String
"""

def test_input_data_type():
    result = check_notes(15)
    assert result == "Not valid data type"


