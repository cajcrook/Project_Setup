def check_notes(notes):
    if notes != str(notes):
        return "Not valid data type"
    elif "#TODO" in notes:
        return True
    else:
        return False