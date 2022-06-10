def reversal1(sentence):
    sentence.strip()

    return " ".join(reversed(sentence.split()))

def reversal2(sentence):
    sentence.strip()

    return " ".join(sentence.split()[::-1])

def reversal_optimal(sentence):

    words = []
    length = len(sentence)
    space = [' ']

    idx = 0
    while idx < length:
        if sentence[idx] not in space:
            word_start = idx

            while idx < length and sentence[idx] not in space:
                idx += 1
            words.append(sentence[word_start:idx])
        idx += 1

    return " ".join(reversed(words))

def reversal3(sentence):
    length, idx, words, space = len(sentence), 0, [], " "

    while idx < length:
        if sentence[idx] != space:
            start = idx
            while idx < length and sentence[idx] not in space:
                idx += 1
            words.append(sentence[start:idx])
        idx += 1
    
    answer, idx = "", len(words) - 1
    
    while idx >= 0:
        answer = answer + words[idx]
        if idx > 0:
            answer = answer + " "
        idx -= 1
    
    return answer

print(reversal1("   Hello John, how are you "))
print(reversal2("   Hello John, how are you "))
print(reversal_optimal("   Hello John, how are you "))
print(reversal3("   Hello John, how are you "))