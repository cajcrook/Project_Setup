# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

The user wants to
Check a string returns a bool: true when it begins with a captial letter and ends with a sentence-ending punctuation mark.
It should also return a check to see how much of the text has passed the test as a %.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
class GrammarStats:
       # User-facing properties
       # type: string

    def __init__(self):
# Parameters:
    # text = str
    Sets the txt to review 
    Returns nothing
    pass

    def check(self, text):
# Parameters:
    # text = str
    return value: bool
    pass


    def percentage_good(self):
# Parameter:
    percentage of text checked so far as a int
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

# Object = Check():

"""
Check a valid string is inputted.
Return if valid return string, else raise False
"""
 grammer_stats = GrammarStats("Hello, it is Friday!")
    assert grammer_stats.check() == True


"""
Check a invalid string is inputted - no puncutation at end.
Return False
"""
 grammer_stats = GrammarStats("Hello, it is Friday")
    assert grammer_stats.check() == False

"""
Check a invalid string is inputted - no capital letter at beginning.
Return False
"""
grammer_stats = GrammarStats("hello, it is Friday!")
    assert grammer_stats.check() == False

"""
Check a invalid string is inputted - no capital letter at beginning or punctuation at end.
Return False
"""
grammer_stats = GrammarStats("hello, it is Friday")
    assert grammer_stats.check() == False


"""
Check for empty string
Return Error Message if empty
"""
with pytest.raises(Exception) as err:
        GrammerStats("")
    assert str(err.value) == "Grammer test requires valid string"

"""
Check input data type == str
Return Error Message if data type != str
"""
with pytest.raises(Exception) as err:
        GrammerStats(1234)
    assert str(err.value) == "Grammer test requires valid string"


# Object = percentage_good():

"""
Check to see how much of the text has passed/ is good based on Check criteria.
Returns int 50
"""
def test_to_check_how_many_texts_have_been_approved():
    grammer_stats = GrammerStats("Hello, it is Friday")
    result = grammer_stats.check()
    assert result == 50









_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
