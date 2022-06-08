def anagram_simple(s1, s2):
    s1, s2 = s1.replace(' ', '').lower(), s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

def anagram_optimal(s1, s2):
    s1, s2 = s1.replace(' ', '').lower(), s2.replace(' ', '').lower()

    #Check for edge cases
    if len(s1) != len(s2): return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for i in count:
        if count[i] != 0:
            return False
    return True