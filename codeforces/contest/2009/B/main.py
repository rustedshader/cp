for _ in range(int(input())):
    n = int(input())
    answer = []
    for _ in enumerate(range(n)):
        arr = list(map(str,input()))
        for index,char in enumerate(arr):
            if char == '#':
                answer.append(index+1)
    print(*answer[::-1])
