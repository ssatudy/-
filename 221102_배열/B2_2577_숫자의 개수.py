a = int(input())
b = int(input())
c = int(input())

summary = a * b * c
st = str(summary)
lst = list(map(int, st))

print(lst.count(0))
print(lst.count(1))
print(lst.count(2))
print(lst.count(3))
print(lst.count(4))
print(lst.count(5))
print(lst.count(6))
print(lst.count(7))
print(lst.count(8))
print(lst.count(9))