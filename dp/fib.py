def fib(n,dp):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n-1,dp) + fib(n-2,dp)
        return dp[n]

dp = [-1] * (21)
print(fib(20,dp))
