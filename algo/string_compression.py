def compress(string):
    # run length compression algorithm

    r = ""
    length = len(string)

    if length == 0: return ""
    if length == 1: return string + '1'

    last = string[0]
    count = 1
    idx = 1

    while idx < length:
        if string[idx] == string[idx - 1]:
            count = 1
        else:
            r = r + string[idx - 1] + str(count)
        idx += 1
    r = r + string[idx - 1] + str(count)
    return r