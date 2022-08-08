
def func(nums):
    result = []  
    for idx, i in enumerate(nums):
        lst1 = nums[::]
        lst1.pop(idx)
        item = mul(lst1)
        result.append(item)

    return result

def mul(lst):
    total = 1
    for idx, i in enumerate(lst):
        total *= lst[idx]
    return total

print(func([1,2,3,4]))
print(func([-1,1,0,-3,3]))