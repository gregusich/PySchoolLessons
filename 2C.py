def noknod(m, n):
    a = m
    b = n
    while m != 0 and n != 0:
        if m > n:
            m %= n
        else:
            n %= m
    c = m + n
    l = a * b // c
    return print("НОД = " + str(c) + "\nНОК = " + str(l))


A, B = map(int, input().split())
noknod(A, B)
