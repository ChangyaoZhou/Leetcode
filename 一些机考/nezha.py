def dfs(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] != 1:
        return 0
    grid[i][j] = 0
    area = 1
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_i = di + i
        new_j = dj + j
        area += dfs(grid, new_i, new_j)
    return area


def max_island(grid):
    result = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                result = max(result, dfs(grid, i, j))
    return result


grid = [[0, 0, 0, 0]]


def min_minute(grid):
    bad_que, good_que = [], []
    m = len(grid)
    n = len(grid[0])
    step = 0
    num_good = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                bad_que.append((i, j))
            elif grid[i][j] == 1:
                num_good += 1
                #good_que.append((i, j))

    while bad_que:
        #new_que = []
        #for i, j in bad_que:
        size = len(bad_que)
        for _ in range(size):
            i, j = bad_que.pop(0)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i = i + di
                new_j = j + dj
                if new_i >= 0 and new_i <= m - 1 and new_j >= 0 and new_j <= n - 1 and grid[new_i][new_j] == 1:
                    grid[new_i][new_j] == 2
                    bad_que.append((new_i, new_j))
                    num_good -= 1
                    #good_que.remove((new_i, new_j))
                if num_good == 0:
                    return step
        #bad_que = new_que
        step += 1



