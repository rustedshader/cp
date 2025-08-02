for _ in range(int(input())):
    a, b = map(int,input().split(" "))
    c_value = 0
    for index,c in enumerate(range(a,b)):
        if index == 0:
            c_value = (c-a)+(b-c)
        else:
            c_value = min((c-a)+(b-c),c_value)
    print(c_value)
