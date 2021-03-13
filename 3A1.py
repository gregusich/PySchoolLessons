def isPerfect(n):
    summ = 0
    for x in range(1, n):
        if n % x == 0:
            summ += x
    return print(summ == n)


A = int(input())
isPerfect(A)