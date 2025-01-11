def fac(n):
    if n < 0:
        return "Enter Positive Integer !"
    if n == 1 or n==0:
        return 1
    return n*fac(n-1)

print(fac(5))
