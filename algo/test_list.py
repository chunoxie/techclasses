def testing(lst):
    new_list = list(lst)
    for i in range(len(lst) + 1):
        print(i, new_list.pop())

data = "{{]]}}("
testing(data)