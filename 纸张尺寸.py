import os
import sys
st = input()
m = 1189
n = 841
t = int(st[1])
for i in range(t):
    m = m//2
    if n > m:
        m,n = n,m
print(m)
print(n)
