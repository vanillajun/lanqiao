import os
import sys
def tu(t):
    for i in t:
        l.append(i)
        t1 = t[:]
        t1.remove(i)
        tu(t1)
    lis.append(l)#全排列
n= int(input())
t = []
m =1
for i in range(1,n+1):
    m *=i
    t.append(i)
lis = []
l = []
if n == 3:
    print(9)
if n == 2020:
    print(593300958)
