def fib(c):
    f1 = 1
    d = 2
    print(f1, end=" ")
    f2 = 1
    print(f2, end=" ")
    while d != c:
        f1 = f1 + f2
        print(f1, end=" ")
        d += 1
        if d == c:
            break
        f2 = f2 + f1
        print(f2, end=" ")
        d += 1


c = int(input())
fib(c)

