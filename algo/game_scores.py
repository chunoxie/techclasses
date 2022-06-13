def game_scores(ops):
    result = []

    for i in range(len(ops)):
        if ops[i].isnumeric():
            result.append(int(ops[i]))
        if ops[i] == "+":
            result.append(result[-1] + result[-2])
        if ops[i] == "D":
            result.append(2 * result[-1])
        if ops[i] == "C":
            result.pop()

    return sum(result)

lst = ["5", "2", "C", "D", "+"]

print(game_scores(lst))