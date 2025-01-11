for _ in range(int(input())):
    n,m = map(int,input().split(" "))
    a = []
    b = []
    x = 0
    y = 1
    for _ in range(n):
        a.append(list(map(int,list(input()))))
    for _ in range(n):
        b.append(list(map(int,list(input()))))

    print(a,b)
    # for i in range(n*m):
    #     if(x>m-1):
    #         x = x-m+1
    #         y +=1
    #     else:
    #         x += 1
    #     print("x is",x,"y is",y,a[i])
    # print()
    # print()
    # print("----------")
