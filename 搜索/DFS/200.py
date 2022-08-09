def dfs(grid, cur_i, cur_j):
    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != '1':
        # 如果搜索走出了board的范围，或者不再是1了，就停止
        return 0
    grid[cur_i][cur_j] = '0'
    tmp = 1
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_i = cur_i + di
        next_j = cur_j + dj
        tmp += dfs(grid, next_i, next_j)
    return tmp


def numIslands(grid):
    """
    类似695题，先找出以每个位置开始的可能的岛屿，然后输出有多少个
    """
    count = 0
    tmp = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(grid, i, j) > 0:
                count += 1
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(numIslands(grid))

