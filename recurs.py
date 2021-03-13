import sys

sys.setrecursionlimit(5000)


def hanoi(n, a, c, b):
    n = int
    if n != 0:
        hanoi(n - 1, a, b, c)
        print('Move the plate from', a, 'to', c)
        hanoi(n - 1, b, c, a)


hanoi(n, a, c, b)
