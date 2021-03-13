from random import randint

N = int(input())
A = [randint(1, 100)
     for i in range(1, N + 1)]
print(*A)
B = [A[i] for i in range(1, N, 2)]
print(*B)
A = B
print(*A)