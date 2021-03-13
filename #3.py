# 3
k = list(map(int, input().split()))
for i in range(1, len(k)):
    if ((k[i-1] % 2 == 0) and (k[i] % 2 == 1)) or ((k[i-1] % 2 == 1) and (k[i] % 2 == 0)):
        print("YES")
    else:
        print("NO")
