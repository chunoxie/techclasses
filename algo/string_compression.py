def compress1(string):
    # run length compression algorithm
    r = ""
    length = len(string)

    if length == 0: return ""
    if length == 1: return string + '1'

    #last = string[0]
    count = 1
    idx = 1

    while idx < length:
        if string[idx] == string[idx - 1]:
            count += 1
        else:
            r = r + string[idx - 1] + str(count)
            count = 1
        idx += 1

    r = r + string[idx - 1] + str(count)
    return r

def compress2(string):
    if not string: return ""
    length = len(string)

    if length == 1: return string + '1'
    count = 1
    result = ""

    for idx in range(1, length):
        if string[idx] == string[idx - 1]:
            count += 1
        else:
            result += string[idx - 1] + str(count)
            count = 1

    result += string[-1] + str(count)
    return result

print(compress1("AAaaCcc"))
print(compress2("AAaaCcc"))