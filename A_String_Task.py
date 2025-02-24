def solve(s: str):
    vow = ['a','e','i','o','u','y']
    ans = ''
    for char in s.lower():
        if char in vow:
            continue
        else:
            ans += '.'+char
    
    print(ans)


s = input()
solve(s)
