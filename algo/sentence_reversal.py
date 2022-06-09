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

    "   Hello John, how are you "