import time
from tracemalloc import start


start = time.time()
def func(nums):
    result = []
    nums = sorted(nums)            # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            summary = nums[i] + nums[l] + nums[r]
            if summary < 0:
                l += 1
            elif summary > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return result

print(func([1,2,-2,-1]))
print("time :", time.time()-start)
print(func([-1,0,1,2,-1,-4]))
print("time :", time.time()-start)
print(func([-1,0,1,0]))
print("time :", time.time()-start)
print(func([-2,0,1,1,2]))
print("time :", time.time()-start)
