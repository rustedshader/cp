x = 0
def solve(inp: str):
    global x
    if inp == "++X" or inp == "X++":
        x+=1
    if inp == "--X" or inp == "X--":
        x-=1



for _ in range(int(input())):
    solve(input())

print(x)