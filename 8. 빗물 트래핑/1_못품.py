
def func(lst):
    result = 0
    num = 0
    for_j = 0
    for i in lst:
        start = 0
        for_j += 1
        for j in lst[for_j:]:
            start += 1
            num += 1         
            if i == 0:
                break
            elif i > j:
                for _ in lst[for_j+1:]:
                    if i < _:
                        result += (i - j)
                        lst.pop(for_j+start-1)             
                        lst.insert(for_j+start-1, 0)
                        break
                    elif (i > _) and (_ > j):
                        result += (_ - j)
                        lst.pop(for_j+start-1)             
                        lst.insert(for_j+start-1, 0)
                        break

            else:
                break
    return result

print(func([0,1,0,2,1,0,1,3,2,1,2,1]))
print(func([0,1,0,2,1,0,1,3,2,1,2,1]))
print(func([4,2,3]))
print(func([4,2,0,3,2,5]))
