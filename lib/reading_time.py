def reading_time(text):
    words = text.split()
    word_count = len(words)
    time = word_count / 200
    return time