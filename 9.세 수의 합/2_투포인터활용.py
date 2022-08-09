
def func(lst):
    result = []
    lst = sorted(lst)            # [-4, -1, -1, 0, 1, 2]
    for i in range(len(lst)-2):
        l, r = i+1, len(lst)-1

        while l < r:
            summary = lst[i] + lst[l] + lst[r]
            if summary == 0 and sorted(list((lst[i], lst[l], lst[r]))) not in result:
                result.append(sorted(list((lst[i], lst[l], lst[r]))))
                l += 1
                r -= 1
            elif summary > 0:
                r -= 1
            elif summary < 0:
                l += 1
            else:
                break
    return result

print(func([1,2,-2,-1]))
print(func([-1,0,1,2,-1,-4]))
print(func([-1,0,1,0]))
print(func([-2,0,1,1,2]))
