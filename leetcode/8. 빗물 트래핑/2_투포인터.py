import time
from tracemalloc import start

start = time.time()
def trap(height):
    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max),  max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume
print("time :", time.time()-start)
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print("time :", time.time()-start)
print(trap([4,2,0,3,2,5]))
print("time :", time.time()-start)
print(trap([4,2,3]))
print("time :", time.time()-start)



