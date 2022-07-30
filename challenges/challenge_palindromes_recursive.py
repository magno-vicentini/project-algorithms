def is_palindrome_recursive(word, low_index, high_index):
    check_odd_string = high_index - low_index

    if(word == ''):
        return False

    if check_odd_string == 1 and word[low_index] == word[high_index]:
        return True

    if low_index == high_index:
        return True

    if low_index == 0 and high_index == 1:
        return True

    if word[low_index] != word[high_index]: 
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
