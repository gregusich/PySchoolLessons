from random import randint

N = int(input())
A = [randint(1, 100)
     for i in range(1, N + 1)]
print(*A)
for i in range(1, N + 1, 2):
    for j in range(1, N - i - 1, 2):
        if A[j] < A[j + 2]:
            A[j], A[j + 2] = A[j + 2], A[j]
print(*A)
