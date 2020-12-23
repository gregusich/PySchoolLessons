# задача 3510
x_f = int ( input ())
y_f = int ( input ())
x_t = int ( input ())
y_t = int ( input ())
if abs ( x_f  - x_t ) <= 1 and abs ( y_f  - y_t ) <= 1:
    print ('YES')
else:
    print ('NO')
