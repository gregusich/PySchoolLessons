def bsort():
    a = list(map(int, input().split()))
    n = len(a)
    d = []
    for i in range(n):
        if i % 2 == 0:
            d.append(i)
        elif i == 0:
            d.append(a[0])
    n = len(d)
    for i in range(n):
        for j in range(n - i - 1):
            if d[j] < d[j + 1]:
                d[j], d[j + 1] = d[j + 1], d[j]
    print(*d)


bsort()
