import pytest
from lib.diary_entry import DiaryEntry

"""Given empty title and contents
returns error message
"""
def test_empty_title_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entry must have title and/or content"

"""
Given a title and content
returns a formated entry: My title: this is my content
"""

def test_format_title_and_content():
    diary_entry = DiaryEntry("My title", "this is my content")
    result = diary_entry.format()
    assert result == "My title: this is my content"

"""
Given a title and content
count_words returns number of words in _title and _contents
"""
def test_counts_words():
    diary_entry = DiaryEntry("My title", "this is my content")
    result = diary_entry.count_words()
    assert result == 6

"""
Given a WPM of 2
test with 2 words
reading_time returns est reading time based on WPM and content: 4
"""
def test_reading_time_2wpm_2words():
    diary_entry = DiaryEntry("My title", "one two")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a WPM of 2
test with 4 words
reading_time return 2 minutes
"""
def test_reading_time_2wpm_4words():
    diary_entry = DiaryEntry("My title", "one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a WPM of 2
given a minutes 1
reading_chunks returns 2 words from string
"""
def test_reading_chunks_2wpm_1min():
    diary_entry = DiaryEntry("My title", "one two three four five six seven eight nine ten eleven twelve")
    result = diary_entry.reading_chunk(2,1)
    assert result == ("one two")

"""
Given a WPM of 2
given a minutes 3
reading_chunks returns 6 words from string
"""
def test_reading_chunks_2wpm_1min():
    diary_entry = DiaryEntry("My title", "one two three four five six seven eight nine ten eleven twelve")
    result = diary_entry.reading_chunk(2,3)
    assert result == ("one two three four five six")

"""
given contents of 6 words
Given a WPM of 2
given a minutes 1
Firs time reading_chunk returns "one two"
Next time returns "three four"
"""
def test_reading_chunks_2wpm_1min_called_twice():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,1) == "three four"

"""
given contents of 6 words
Given a WPM of 2
given a minutes 1
Firs time reading_chunk returns "one two"
Next time returns "three four"
Next time returns "five six"
"""
def test_reading_chunks_2wpm_1min_called_multiple_times():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,1) == "three four"
    assert diary_entry.reading_chunk(2,1) == "five six"

"""
given contents of 6 words
Given a WPM of 2
given a minutes 1
Firs time reading_chunk(2,1) return "one two"
Next time reading_chunk(1,1) return "three"
Next time reading_chunk(2,1) return "four five"
"""
def test_reading_chunks_wpm_variable_1min_():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(1,1) == "three"
    assert diary_entry.reading_chunk(2,1) == "four five"   

"""given a contents of 6 words
if readin_chunk is called repeatly
the last chunk is the last words in the text, even if shorter than readign time
the next chunk after that starts again
"""
def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2,2) == "one two three four"
    assert diary_entry.reading_chunk(2, 2) == "five six"
    assert diary_entry.reading_chunk(2,2) == "one two three four"

"""given a contents of 6 words
if readin_chunk is called repeatly
the last chunk is the last words in the text, even if shorter than readign time
the next chunk after that starts again
"""
def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2,2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2,2) == "one two three four"

