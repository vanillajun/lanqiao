import os
import sys
# 请在此输入您的代码
str = input()
num = 0
b= []
for s in str :
  num1 = str.count(s)
  if num1 > num :
    num = num1
for tr in str :
  if str.count(tr) == num :
    b.append(tr)
#出现最多次数有多个字母时，从小到大排序，字典序最小的那个输出
#列表排序
b.sort()
print(b[0])
print(num)
