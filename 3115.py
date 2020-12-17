# задача 3515
n = int ( input ())
m = int ( input ())
k = int ( input ())
#if ( n * m ) // 2 == k and ( n * m ) % 2 == 0:
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print ('YES')
else:
    print ('NO')
