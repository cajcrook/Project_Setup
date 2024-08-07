# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


## 2. Design the Function Signature

def check_grammer(text):
# parameter
    text = a string eg "Hello world!"
# return
    A boolean - True or False


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

''' python
"""
Input string with capital letter at beginning and . at the end.
Returns True.

def check_grammer("Hello everyone!")
    => True
"""

"""
Input string with capital letter at beginning and ? at the end.
Returns True.

def check_grammer("Hello everyone!")
    => True
"""

"""
Input string with capital letter at beginning and ! at the end.
Returns True.

def check_grammer("Hello everyone!")
    => True
"""

"""
Input string with capital letter at beginning and NO punctuation at the end.
Returns False.

def check_grammer("Hello everyone")
    => False
"""

"""
Input string with NO capital letter at beginning but has punctuation at the end.
Returns False.

def check_grammer("hello everyone!")
    => False
"""

"""
Input string with NO capital letter at beginning and NO punctuation at the end.
Returns False.

def check_grammer("hello everyone")
    => False
"""

"""
Input string is empty
Returns Error Case.

def check_grammer("")
    => rasies error
"""

'''python

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
