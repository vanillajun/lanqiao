def factorial(n):
    if n < 1 :
        print('输入错误')
        return -1
    elif n == 1 or n == 2 :
        return 1
    else :
        return factorial(n-1)+factorial(n-2)


n = int(input('输入数列n的大小:'))
m = factorial(n)
print(m)
