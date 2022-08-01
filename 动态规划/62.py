import numpy as np
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    '''
    法一: 动态规划
    建立一个dp二维列表，每一格代表走到该格有几个种可能的路径，由于每一步只能向下或者向右走，
    dp[i][j] = dp[i][j-1] + dp[i-1][j]
    ####### use numpy(more time and space needed) ############
    dp = np.zeros((m, n))
    dp[0, :] = np.ones(n)
    dp[:, 0] = np.ones(m)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return int(dp[m-1][n-1])
    ####### use list instead of numpy #############
    dp = [[1] * n] + [[1] + [0] * (n-1)for i in range(m-1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]
    '''
    # 法二: 排列组合方法
    # 从左上角到右下角的过程中，我们需要移动 m+n-2m+n−2 次，其中有 m-1m−1 次向下移动，n-1n−1 次向右移动。
    # 因此路径的总数，就等于从 m+n-2m+n−2 次移动中选择 m-1m−1 次向下移动的方案数，即组合数：C_(m+n-2)^(m-1)
    step = 1
    for i in range(m-1):
        step = float(step * (m + n - 2 - i) / (m - 1 - i))
    return round(step)

m = 3
n = 7
print(uniquePaths(m, n))



