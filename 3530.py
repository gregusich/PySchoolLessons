#задача 3530
n = int (input())
#k = (  10 ** n ) - 1
for i in range (10**n - 1, 10**(n - 1) - 1, -2 ):
    print( i, end = ' ' )