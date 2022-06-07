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