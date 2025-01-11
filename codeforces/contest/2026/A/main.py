for _ in range(int(input())):
    X,Y,K = map(int,input().split(" "))
    ax , ay = 0 , 0
    bx , by = min(X,Y) , min(X,Y) 
    cx , cy = 0 , min(X,Y)
    dx ,  dy = min(X,Y),0
    print(ax,ay,bx,by)
    print(cx,cy,dx,dy)

