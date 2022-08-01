def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    同62题，建立一个dp二维列表，每一格代表走到该格有几个种可能的路径，obstacle处可能的路径为0，
    dp[i][j] = dp[i][j-1] + dp[i-1][j]
    注意: obstacle也有可能出现在上边缘和左边缘上，此时 dp[i][j] = dp[i][j-1] 或 dp[i-1][j]
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[1] * n] + [[1] + [0] * (n - 1) for i in range(m - 1)]
    for i in range(0, m):
        for j in range(0, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))