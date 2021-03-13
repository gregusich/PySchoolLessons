# 1
spisock = list(map(int, input().split()))
f_max = spisock[0]
f_min = spisock[0]
max_ind = 0
for i in range(1, len(spisock)):
    if spisock[i] < f_min:
        f_min = spisock[i]
for i in range(1, len(spisock)):
    if spisock[i] > f_max:
        f_max = spisock[i]
        max_ind = i
spisock[max_ind] = f_min
print(spisock[max_ind])
