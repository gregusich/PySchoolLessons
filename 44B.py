from random import randint

N = int(input())
A = [randint(1, 100)
     for i in range(1, N + 1)]
print(*A)
m = min(A)
'''for i in range(1, N+1):
    if m < A[i]:
        m = A[i]'''
print(m)
for i in range(1, A.index(m)):
    for j in range(A.index(m) + 1 - i - 1):
        if A[j] < A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print(*A)
