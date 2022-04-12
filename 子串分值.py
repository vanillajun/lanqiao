import os
import sys

# 请在此输入您的代码
#关于字符串子串的定义：连续的字符串片段
#找一个框，框的大小从1-5，来挑选子串
def sumt(st): #计算字符串出现一次的字符个数
  su = 0
  for i in st:
    num = st.count(i)
    if num == 1:
      su += 1
  return su
#拆分字符串：
st_ = input()
#n = 1 #子串长度
sumn = 0
for n in range(1,len(st_)+1):
  for i in range(len(st_)):
    if i + n <= len(st_):
      stn = st_[i:i+n]
      sumn += sumt(stn)
      print(stn)
print(sumn)
