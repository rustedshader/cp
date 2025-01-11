for _ in range(int(input())):
    arr = []
    a = input()
    b = input()
    sum = 0
    for char in b:
        if char not in a:
            arr.append(char)
        elif char in a:
            if a.count(char) < b.count(char):
                sum = b.count(char) - a.count(char)
    print(len(arr)+len(a)+sum)
    # Bug at test case 2 line 157
