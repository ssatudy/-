def func(nums, target):
    result = []
    nex = 0
    for i in nums[:-1]:
        nex += 1
        for j in nums[nex:]:
            if i + j == target:
                result.append(nums.index(i))
                nums.pop(result[0])
                nums.insert(result[0], 'a')
                result.append(nums.index(j))
                return result

print(func([1, 2, 5, 3], 8))
print(func([2, 7, 11, 15], 9))
print(func([1, 2, 3, 4], 4))
print(func([3, 3], 6))
print(func([2, 7, 11, 15], 9))
