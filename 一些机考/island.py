def dfs(i, j, grid):
    m = len(grid)
    n = len(grid[0])
    if i > m-1 or i < 0 or j > n-1 or j < 0 or grid[i][j] != 1:
        return 0

    grid[i][j] = 0
    island = 1
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_i = di + i
        next_j = dj + j
        island += dfs(next_i, next_j, grid)
    return island


def count_island(grid):
    count = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if dfs(i, j, grid) > 0:
                count += 1
    return count


grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]]

print(count_island(grid))
