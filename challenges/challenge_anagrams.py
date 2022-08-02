
def is_anagram(first_string, second_string):

    first_str = list(first_string.lower())
    second_str = list(second_string.lower())

    if (len(first_str) != len(second_str)):
        return False

    for value in first_str:
        try:
            second_str.remove(value)
        except ValueError:
            return False

    return True
