import os
import sys
#n = int(input())
# 冒泡排序，相邻的两个字符进行交换
v = eval(input())
dp = [[[0 for i in range(26)]for j in range(26)]for i in range(26)]
for i in range(1,26):
    dp[0][i][1] = dp[0][i-1][1] + i #最大交换形式
for i in range(1,26):
    for n in range(2,26):
        dp[i][i-1][n] = n*(i-1)+dp[i-1][i-1][n]#前i个重复n次的字符
    for n in range(2,26):
        for j in range(i,26):
            dp[i][j][n] = dp[i][j-1][n]+i+j#i个重复2次的字符,之后的字符串长度是j
for i in range(0,26):
    for j in range(i,26):
        if v in dp[i][j]:#找到交换是v的字符串
            c = dp[i][j].index(v)
            b = i #重复次数
            a = j
        break
zm=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer = []
for i in range(b):
    answer.append(c*zm[i])
for i in range(b,a+1):
    answer.append(zm[i])
answer.reverse()
x = ''
for i in answer:
    x+=i
print(x)
