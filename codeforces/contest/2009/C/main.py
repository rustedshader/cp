for _ in  range(int(input())):
    x,y,k = map(int,input().split(" "))
    if int(abs((y+k-1)/k)) >= int(abs((x+k-1)/k)):
        print(2*(int(abs((y+k-1)/k))))
    if int(abs((y+k-1)/k)) < int(abs((x+k-1)/k)):
        print(2*int(abs((x+k-1)/k))-1)
