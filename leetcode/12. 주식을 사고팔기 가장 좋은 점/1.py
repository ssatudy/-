def func(lst):
    counts = 0       # 책 보고 배움...
    mini = 9999999999999999999999
    for i in lst:
        mini = min(mini, i)
        counts = max(counts, i - mini)
    return counts

# print(func([2,4,1]))
print(func([7,1,5,3,6,4]))