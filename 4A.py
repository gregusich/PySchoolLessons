def bsort():
    a = list(map(int, input().split()))
    n = len(a)
    d = []

    n = len(d)
    for i in range(n):
        for j in range(n - i - 1):
            if d[j] < d[j + 1]:
                d[j], d[j + 1] = d[j + 1], d[j]
    print(*d)


bsort()
