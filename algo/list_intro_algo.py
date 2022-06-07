def method1():
    l = []
    for n in range(10000):
        l = l + [n]

def method2():
    l = []
    for n in range(10000):
        l.append(n)

def method3():
    l = [n for n in range(10000)]

def method4():
    # as per time complexity, built-in functions are most effective
    l = list(range(10000))

