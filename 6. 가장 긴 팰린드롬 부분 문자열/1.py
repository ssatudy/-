def func(s):
    if s == s[::-1]:
        return s
    
    lst = []     # ['c', 'bb', 'b', 'b', 'd']
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if s[i:j] == s[i:j][::-1]:
                lst.append(s[i:j])
    
    result = ''
    num = 0
    for i in lst:
        if len(i) > num:
            num = len(i)
            result = i
    return result

print(func('babad'))
print(func('cbbd'))