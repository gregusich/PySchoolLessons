def drob(m, n):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return print(str(m // k) + '/' + str(n // k))
        else:
            k -= 1
    return print(str(m) + '/' + str(n))


A, B = map(int, input().split())
drob(A, B)

