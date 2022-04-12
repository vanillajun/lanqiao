import os
import sys
for n in range(1,100000000000):
    i = (n*6+1)*11*17
    if i % 2 == 1 and i%3 == 2 and i%4 == 1 and i%5 ==4 and i%6 == 5 and i%7 == 4 and i%8 == 1 and i%9 == 2 and i%10 == 9 and i%12 == 5 and i%13 == 10 and i%14 == 11 and i%15 == 14 and i%16 == 9 and i%18 == 11 and i%19 == 18 and i%20 == 9 and i%21 == 11 and i%22 == 11 and i%23 == 15 and i%24 == 17 and i%25 == 9 and i%26 == 23 and i%27 == 20 and i%28 == 25 and i%29 == 16 and i%30 == 29 and i%31 == 27 and i%32 == 25 and i%33 ==11 and i%34 == 17 and i%35 == 4 and i%36 == 29 and i%37 == 22 and i%38 == 37 and i%39 == 23 and i%40 == 9 and i%41 ==1 and i%42 == 11 and i%43 == 11 and i%44 == 33 and i%45 == 29 and i%46 == 15 and i%47 == 5 and i%48 == 41 and i%49 == 46:
        print(i)
        break
print(123)
