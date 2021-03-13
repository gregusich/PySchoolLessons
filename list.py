def f(v):
    res = ""
    while True:
        rem = v % -2
        v //= -2
        if rem < 0:
            rem += 2
            v += 1
        if rem == 1:
            res = "1" + res
        if rem == 0:
            res = "0" + res
        if v == 0:
            break
    print(res)


c = int(input())
f(c)

