n=int(input())
list1=[]
for n in range(n):
    row=[1] # 第一行第一列为1
    list1.append(row)

    if n==0:
        for num in row:  # 这里主要是为输出做的格式处理
            print(num,end=" ")
            print()
        continue
    for m in range(1,n):
        row.append(list1[n-1][m-1]+list1[n-1][m])
    row.append(1)

    for num in row:
        print(num, end=" ")
    print()
