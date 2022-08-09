
def func(lst):       # a, b에 앞에서 곱한 값, 뒤에서 곱한 값으로 풀어야됨
    a = [1 for i in lst]
    b = [1 for i in lst]
    results = []

    for i in range(1, len(lst)):
        a[i] = a[i - 1] * lst[i - 1]
        
    for i in range(len(lst) - 2, -1, -1):
        b[i] = b[i + 1] * lst[i + 1]
    
    for p1, p2 in zip(a, b):
        results.append(p1 * p2)
    return results    

print(func([1,2,3,4]))
print(func([-1,1,0,-3,3]))
