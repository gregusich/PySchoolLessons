# 3832
def nears(k):
    k = list(map(int, input().split()))
    for i in range(1, len(k)):
        if k[i-1] * k[i] > 0:
            print(k[i-1], k[i])
            break


nears(k=str)
