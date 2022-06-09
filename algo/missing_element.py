import collections


def find_element(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2: return num1
    
    return arr1[-1]

def find_element2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

def find_element_xor(arr1, arr2):
    result = 0

    for num in arr1+arr2:
        # more info needed on XOR operation
        result^=num
        print(result)
    return result

# for a, b in zip([1,2,3], [4,5,6]):
#     print(f'a is: {a}; b is: {b}')
# unpacks the list as tuple: 1,4 2,5 3,6
find_element_xor([5,7,7,8], [5,7,8])