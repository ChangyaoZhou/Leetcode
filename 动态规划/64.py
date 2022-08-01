def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    建立一个dp二维列表，dp[i]表示每一格代表走到该格的路径上的数字最小和
    因为每一步只能向下或向右，则每一格中的dp值为grid中当前格的值 + 相邻(左，上)两个dp值中的较小值
    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
    """
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            # 边缘上只能加一个值
            elif i == 0:
                dp[i][j] = grid[i][j] + dp[i][j - 1]
            elif j == 0:
                dp[i][j] = grid[i][j] + dp[i - 1][j]
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]

grid = [[1,3,1],
        [1,5,1],
        [4,2,1]]
#grid = [[1]]
print(minPathSum(grid))