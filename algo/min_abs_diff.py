def min_abs_diff(arr):
    arr.sort()
    result = []
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        result.append([diff, arr[i-1], arr[i]])

    result.sort()

    for item in result:
        print(item[-2], item[-1])
    #return result

lst = [-2, 1, 4, 8, 2, 9, -10, 0]

min_abs_diff(lst)