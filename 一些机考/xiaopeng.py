def num_stairs(n):
    #dp = [0 for i in range(n+1)]
    #dp[0] = 1
    #dp[1] = 1
    dp = [1, 1]
    for i in range(2, n+1):
        tmp = dp[0]
        dp[0] = dp[1]
        dp[1] = tmp + dp[1]
        #dp[i] = dp[i-1] + dp[i-2]
        print(dp)
    return dp[1]


n = 3
print(num_stairs(n))
