def fib(n: int) -> int:
    '''
    斐波那契数列
    F(0) = 0，F(1) = 1
    F(n) = F(n - 1) + F(n - 2)，其中 n > 1
    '''
    dp = []
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp.append(0)
    dp.append(1)
    for i in range(2, n+1):
        dp.append(dp[i - 1] + dp[i - 2])
        print(dp)
    return dp[-1]

n = 4
print(fib(n))
#fib = [0, 1, 1, 2, 3], fib[4] = 3