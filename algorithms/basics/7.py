N = int(input())
space = N - 1
star = 1

for _ in range(N):
    print(' ' * space + '*' * star,' '*space)
    star += 2
    space -= 1
