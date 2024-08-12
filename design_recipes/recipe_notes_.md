# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def check_notes():
parameters: string

return boolean True or False


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

""""
Input - string including #TODO eg "I've a task #TODO"
Output - True
"""

""""
Input - string excluding #TODO eg "I've a task"
Output - False
"""

"""
Check data type eg. 101.1
Return Not valid if not String
"""


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
