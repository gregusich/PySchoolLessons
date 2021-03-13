from random import randint

N = int(input())
K = int(input())
A = [randint(1, 100)
     for i in range(1, N + 1)]
print(*A)
