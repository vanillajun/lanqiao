import os
import sys
def ston(st):
    se = set()
    for i in range(len(st)-2):
        if (st[i]!= st[i+1] and st[i+1]==st[i+2]) or (st[i]==st[i+1] and st[i+1]!=st[i+2]):
            se.add(st[i])
            se.add(st[i+1])
            se.add(st[i+2])
    st = list(st)
    st_ = st[:]
    st = set(st)
    st_ = set(st_)
    for i in st:
        if i in se:
            st_.remove(i)
    return st_
st = input()
for i in range(100000):
    st = ston(st)
    if len(st) == 0:
        print('EMPTY')
        break
if len(st)!= 0:
    print(list(st)[0])
        
