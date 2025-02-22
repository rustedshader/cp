count = 0

def solve(n: int):
    if n == 0:
        return
    global count
    if n >= 5:
        count += n // 5 
        solve(n%5)
    elif n >= 4 and n < 5:
        count += n // 4
        solve(n % 4 )
    elif n >= 3 and n < 4:
        count += n // 3
        solve(n % 3)
    elif n >= 2 and n < 3:
        count += n // 2
        solve(n % 2 )
    elif n >= 1 and n < 2:
        count += n // 1
        solve(n % 1 )
    else:
        return


n = int(input())
solve(n)
print(count)