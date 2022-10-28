def is_anagram(first_string, second_string):
    if (first_string == "" or second_string == ""):
        return False
    first = first_string.lower()
    second = second_string.lower()
    for letra in first:
        if (first.count(letra) != second.count(letra)):
            return False
        if (letra not in second):
            return False
    else:
        return True
