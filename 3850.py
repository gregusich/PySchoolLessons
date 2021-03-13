
for i in reversed(range(len(lst))):
    if lst[i] == '0':
        lst.append(lst.pop(i))
print(*lst)


a = list(map(int, input().split()))
c = a.count(0)
s = "0" * c
s = list(s)
for i in a:
    a.pop(a.index(0))
a = a + s
print(*a)

