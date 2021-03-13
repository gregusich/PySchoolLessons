def presentDigits(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return print(m == 1)


A, B = map(int, input().split())
presentDigits(A, B)