def bsort():
    a = list(map(int, input().split()))
    n = len(a)
    d = []
    for i in range(n):
        if i % 2 == 1:
            d.append(i)
    n = len(d)
    for i in range(n):
        for j in range(0, n - i - 1):
            if d[j] > d[j + 1]:
                d[j], d[j + 1] = d[j + 1], d[j]
    print(*d)


bsort()
