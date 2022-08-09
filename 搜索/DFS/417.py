def valid_area(cur_x, cur_y, m, n):
    return 0 <= cur_x < m and 0 <= cur_y < n


def dfs(cur_i, cur_j, pre, visited, heights, result_pac):
    # 当heights不在增加，这一个分支的搜索停止
    if heights[cur_i][cur_j] < pre:
        return
    if visited[cur_i][cur_j] == 0:
        visited[cur_i][cur_j] = 1
        result_pac.append([cur_i, cur_j])

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        pre = heights[cur_i][cur_j]
        next_i = cur_i + di
        next_j = cur_j + dj
        # 为了节省时间，只搜索没走过的点
        if valid_area(next_i, next_j, len(heights), len(heights[0])) and visited[next_i][next_j] != 1:
            dfs(next_i, next_j, pre, visited, heights, result_pac)


def pacificAtlantic(heights):
    """
    由于矩阵的左边界和上边界是太平洋，矩阵的右边界和下边界是大西洋，
    因此从矩阵的左边界和上边界开始反向搜索即可找到雨水流向太平洋的单元格，从矩阵的右边界和下边界开始反向搜索即可找到雨水流向大西洋的单元格。

    可以【使用深度优先搜索实现反向搜索】，搜索过程中需要记录每个单元格是否可以从太平洋反向到达以及是否可以从大西洋反向到达。
    反向搜索结束之后，遍历每个网格，如果一个网格既可以从太平洋反向到达也可以从大西洋反向到达，
    则该网格满足太平洋和大西洋都可以到达，将该网格添加到答案中。

    visited_pac表示反向搜索能流到太平洋的点时经过的所有点，即能流到太平洋的所有点，visited_atl同理，
    所以也可以用visited_pac和visited_atl中都为1的格子的坐标得到结果

    """
    m = len(heights)
    n = len(heights[0])
    visited_pac = [[0] * n for i in range(m)]
    visited_atl = [[0] * n for i in range(m)]
    result_pac = []
    result_atl = []
    result = []

    for i in range(m):
        dfs(i, 0, -1, visited_pac, heights, result_pac)
        print(result_pac)
        dfs(i, n-1, -1, visited_atl, heights, result_atl)
    for j in range(n):
        dfs(0, j, -1, visited_pac, heights, result_pac)
        dfs(m-1, j, -1, visited_atl, heights, result_atl)
        #print(visited_pac)
    #print(result_pac)
    #print(result_atl)
    for i in range(m):
        for j in range(n):
            if visited_atl[i][j] == 1 and visited_pac[i][j] == 1:
                result.append([i, j])
    return result
    # print(list(set(result_pac).intersection(set(result_atl))))


heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]
print(pacificAtlantic(heights))
