def climbStairs(n):
    """
    :type n: int
    :rtype: int
    定义一个数组 dp 存储上楼梯的方法数（为了方便讨论，数组下标从 1 开始），dp[i] 表示走到第 i 个楼梯的方法数目。
    第 i 个楼梯可以从第 i-1 和 i-2 个楼梯再走一步到达，走到第 i 个楼梯的方法数为走到第 i-1 和第 i-2 个楼梯的方法数之和。
    dp[i] = dp[i-1] + dp[i-2]

    """
    if n == 1 or n == 2:
        return n
    else:
        dp = []
        dp.append(1)
        dp.append(2)
        print(dp)
        for n in range(2, n):
            dp.append(dp[-1] + dp[-2])
        print(dp)
        return dp[-1]

n = 6
print(climbStairs(n))