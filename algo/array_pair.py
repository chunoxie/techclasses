def pair_sum(arr, target):
    if len(arr) < 2: return

    #Track seen elements
    seen = set()
    output = set()

    for number in arr:
        second_pair = target - number
        if second_pair not in seen:
            seen.add(number)
        else:
            output.add( ((min(number, second_pair)), max(number, second_pair)) )

    return output
    #return '\n'.join(map(str, list(output)))
    #return '\n'.join(map(str, output))