from testclass import Test

def is_prime(n):
    if not isinstance(n, int): return False
    if n < 2: return False

    first_5 = [2, 3, 5, 7, 11]
    if n in first_5: return True

    if n > 11:
        for x in first_5:
            if n % x == 0:
                return False
        return True

test = Test()
test.test_prime(is_prime)