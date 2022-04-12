import os
import sys
import math
N,M = map(int,input().split())
a =[]
b= []
#c = []
num = 0
for i in range(N):
    a.append(list(map(int,input())))
for i in range(N):
    b.append(a[i][0])
    #c.append(a[i][1])
for i in range(1,M+1):    
    num+=max(b)
    tag = max(b)
    t = b.index(tag)
    b[t] = math.reil(b[t]/c[t])
print(num)
