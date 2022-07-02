def balanced_brackets(strings):
    length = len(strings)
    if length < 2 or length % 2 != 0:
        return False

    brackets = {'(': ')', '[': ']', '{': '}'}

    if strings[0] not in brackets:
        return False

    stack = []
    i = 0

    while i < length:
        if strings[i] in brackets:
            stack.append(strings[i])
        else:
            try:
                closing = stack.pop()
                if strings[i] != brackets[closing]:
                    return False
            except Exception as e:
                # print("Exception occured...", e)
                return False
        i += 1
    
    return stack == []

lst = "(())))"
print(balanced_brackets(lst))