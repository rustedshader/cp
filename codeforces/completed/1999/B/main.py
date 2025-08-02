for _ in range(0,int(input())):
    a,b,c,d = map(int,input().split())
    won = 0
    if a>c and b>d or a>c and b==d or b>d and a==c:
        won+=1
    if a>d and b>c or a>d and b==c or b>c and a==d:
        won+=1
    if b>d and a>c or b>d and a==c or a>c and b==d:
        won+=1
    if b>c and a>d or b>c and a==d or a>d and b==c:
        won+=1
    print(won)
