import os
import sys

# 请在此输入您的代码
# = True
for i in range(10000):
  x = i*2019
  n = x
  tag = True
  while n / 10 >= 1:
    m = n % 10 #取一位
    if m % 2 != 0:
      n = n//10
    else:
      tag = False
      break
  if tag: 
    if n % 2 != 0:
      print(x)
      break
