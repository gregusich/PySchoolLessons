# задача 3516
a = int ( input ())
b = int ( input ())
x = ( - b ) // a
if a == 0 and b == 0:
    print('INF')
elif a!=0 and (b==0 or abs(a)<=abs(b)) and (b % a) == 0:
    print(x)
else:
    print('NO')