# 3833
def biggrs(k):
    k = list(map(int, input().split()))
    count = 0
    for i in range(1, len(k)-1):
        if k[i] > k[i+1] and k[i] > k[i - 1]:
            count += 1
        if i+1 > len(k):
            break
    print(count)


biggrs(k=str)
