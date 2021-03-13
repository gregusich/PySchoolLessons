def toprime(N):
    n = int
    for i in range(len(N)):
        for j in range(len(N) - i - 1):
            if N[j] > N[j + 1]:
                N[j], N[j + 1] = N[j + 1], N[j]
    print(*N)


A = list(map(int, input().split()))
toprime(A)
