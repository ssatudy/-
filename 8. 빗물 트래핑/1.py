
def func(lst):
    result = 0
    num = 0
    start = 0
    for i in lst:
        start += 1
        for j in lst[start:]:
            num += 1
            if i == 0:
                break
            elif i > j and i in lst[i+1:]:
                result += (i - j)
                lst.pop(start)
                lst.insert(start, 0)
            else:
                break
    return result
lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(func(lst))