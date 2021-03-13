from array import *


n = int(input())
A = array.array('i', [])
for i in range(1, n+1):
    A.insert(i, int(input()))
for i in range(1, n+1):
    if i % 2 == 0:
        cout += 1
