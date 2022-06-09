def unique_characters1(string):
    return len(set(string)) == len(string)

def unique_characters2(string):
    char_set = set()

    for letter in string:
        if letter in char_set:
            return False
        else:
            char_set.add(letter)
            
    return True