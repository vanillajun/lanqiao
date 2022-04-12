import os
import sys
n = int(input())
m = int(input()) 
lis = []
for i in range(1,n+1):
    t = 0
    for j in str(i):
        t += int(j)
    lis.append(t)
lis.sort()
for i in range(1,n+1):
    h = 0
    for j in str(i):
        h+= int(j)
    if h == lis[m-1]:
        print(i)
        break
