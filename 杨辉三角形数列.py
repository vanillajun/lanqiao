import os
import sys

# 请在此输入您的代码
#观察规律，杨辉三角形中间的数最大，N
N = int(input())
#构建杨辉三角形，不超过N行,列表的列表
lis = []
tage = False
for i in range(N):
  row= [1] #第一行第一列是1
  lis.append(row)
  if i == 0:
    continue #第一行
  for j in range(1,i):
    row.append(lis[i-1][j-1] + lis[i-1][j]) #添加到行中
  row.append(1) #行尾添加1，row在lis里面实时更新
  for m in row:
    if m == N :
      n = i #前n行数
      num = (n*(n+1)//2)+row.index(m)+1 #第索引列
      tage = True
      break
  if tage:
    break
print(num)
