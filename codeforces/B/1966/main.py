for _ in range(int(input())):
    n,m = map(int,input().split(" "))
    arr = []
    # n -> max(y)
    # m -> max(x)
    for k in range(n):
       for j in range(m):

           print(k,j)




# # # #
# # # #
# # # #
# Possilities of a subrectangle !
# cannot be a straight line cannot be 3 points cannot be vertical horizontal straight line
# atleast [0,1 0,2 1,0 1,1 ] [x,y | x,y>x |  x1 > x , y  | x1 , y1 > y ]
# 1 * 1 can be also the subrectangle !
# Quesiton is for SElECTING WRONG NOT SELECTING RIGHT ONE HAHA
