'''
Take a number n and return sum of all numbers from 0 up to and including n.
'''
def sum1(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum += x
    return final_sum

def sum2(n):
    return (n * (n + 1)) / 2

def f_constant(values):
    print("First item:", values[0])
    print("Last item:", values[-1])

def f_linear(lst):
    for v in lst:
        print(v)

def f_quadratic(lst):
    for item1 in lst:
        for item2 in lst:
            print(item1, item2)

def comp_terms(lst):
    print(lst)
    mid = len(lst) // 2

    for v in lst[:mid]:
        print(v)

    for x in range(10):
        print("Hello World!")

def matcher(lst, target):
    for item in lst:
        if item == target: return True
    return False

def make_list(n):
    # Both space and time complexity here are O(n)
    new_list = []
    for num in range(n):
        new_list.append('new')
    return new_list

def printer(n):
    # space complexity of O(1) even though time complexity is O(n)
    for x in range(n):
        print("Hello World!")