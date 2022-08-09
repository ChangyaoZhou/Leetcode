def dfs(grid, cur_i, cur_j):
    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
        return 0
    # 将走过的，计算过的格子赋值0，不会重复数，使岛屿面积大于实际值
    # 另外，如果后面循环再走到相同岛屿的其他格子，就不用再数一遍了，即每个岛屿都只数一遍
    grid[cur_i][cur_j] = 0
    tmp = 1
    # 在四个方向上进行延申，相当于树的四个字节点
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_i = cur_i + di
        next_j = cur_j + dj
        tmp += dfs(grid, next_i, next_j)
    return tmp


def maxAreaOfIsland(grid):
    max_area = 0
    # 计算从每一格开始的最大岛屿的面积，并且取所有岛屿面积的最大值，
    # 每个岛屿只数一次，因为计算过的格子会赋值0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_area = max(max_area, dfs(grid, i, j))
    return max_area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))

