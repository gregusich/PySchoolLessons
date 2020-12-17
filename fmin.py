# нахождение номера позиции первого наименьшего числа с конца
elem = int(input())
f_min = elem % 10
s_min = elem // 10
p = 1
zch = 0
while s_min != 0:
    if f_min > s_min % 10:
        f_min = s_min % 10
    f_min //= 10
while zch != f_min:
    elem //= 10
    zch = elem % 10
    p += 1
print(p)
