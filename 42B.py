from random import randint


N = int(input())
A = [randint(1, 100)
     for i in range(1, N+1)]
print(*A)
m = A[1]
for i in range(1, N+1, 2):
    if m < A[i]:
        m = A[i]
print(m)
