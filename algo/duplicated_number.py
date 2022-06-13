def duplicated_number(nums):
    num_dict = {}
    result = []

    for i in nums:
        if i in num_dict:
            num_dict[i] += 1
            result.append(i)
        else:
            num_dict[i] = 0

    start = nums.index(result[0])
    next_idx = nums.index(result[0], start + 1)
    interval = nums[next_idx - 1] - nums[next_idx - 2]

    result.append(nums[next_idx - 1] + interval)

    # if we needed to replace the duplicate item with the correct value
    #nums[next_idx] = result[-1]

    return result

lst = [10, 20, 30, 40, 50, 60, 30]
print(duplicated_number(lst))
        