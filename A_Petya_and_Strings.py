def solve(a:str,b:str):
    l = zip(a.lower(),b.lower())
    for item in l:
        if ord(item[0]) > ord(item[1]):
            return 1
        if ord(item[0]) < ord(item[1]):
            return -1
    return 0

a = input()
b = input()
print(solve(a,b))
