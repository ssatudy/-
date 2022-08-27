from functools import reduce
def func(lst):
    result = []
    for idx, i in enumerate(lst):
        lst1 = lst[::]
        lst1.pop(idx)
        num = reduce(lambda x,y:x*y, lst1)
        # ↑ 모듈 불러와도 시간 초과
        result.append(num)
    return result



print(func([1,2,3,4]))
print(func([-1,1,0,-3,3]))
