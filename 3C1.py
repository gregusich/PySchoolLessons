def isPrime(n):
    k = 2
    while k * k <= n and n % k != 0:
        k += 1
    return k * k > n


def superPrime(n):
    c = 0
    if isPrime(n) is False:
        return False
    else:
        for i in range(1, int(len(str(n)))):
            if isPrime(n % 10 ** i) is True and isPrime(n // 10 ** i) is True:
                c += 1
                return print(True)
        if c == 0:
            return print(False)


A = int(input())
superPrime(A)

