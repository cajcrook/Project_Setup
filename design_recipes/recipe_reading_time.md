# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

def reading_time(text):
# parameter
    text: string. 
        Will need to be coverted into list to get count of words len(text)
# return value
    this will be (text(len() // 200)) a float showing the estimated reading time.
# side effets
    parameter text is not string = check type and covert?


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

"""
Input is simple string of 100 word
It returns a est. time of 0.5 of a minute
"""

"""
Input 200 word string
return est time of 1 minute
"""

"""
Input 600 word string
Return est time of 3 min
"""

"""
Input 267 word string
Return est time of 
"""




```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

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
