def bsort():
    a = list(map(int, input().split()))
    k = a.index(max(a))
    l = a.index(min(a))
    m = a[+1:k]
    s = len(m)
    for i in range(s):
        for j in range(s - i - 1):
            if m[j] < m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    print(*m)


bsort()
