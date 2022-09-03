n, m = 5, 5
grid = [['.', '.', '.', '.', '.'],
        ['.', 'R', 'R', 'D', '.'],
        ['.', 'U', '.', 'D', 'R'],
        ['.', 'U', 'L', 'L', '.'],
        ['.', '.', '.', '.', 'O']]


def dfs(i, j, grid, letter_map):
    m = len(grid)
    n = len(grid[0])
    if i >= m or j >= n or i < 0 or j < 0:
        return False
    if grid[i][j] == 'O':
        return True
    elif grid[i][j] == '.':
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i = di + i
            next_j = dj + j
            if dfs(next_i, next_j, grid, letter_map):
                return True
    else:
        di, dj = letter_map[grid[i][j]]
        next_i = di + i
        next_j = dj + j
        if not dfs(next_i, next_j, grid, letter_map):
            return False


def func(m, n, grid):
    letter_map = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}
    dead_count = 0
    for i in range(m):
        for j in range(n):
            if not dfs(i, j, grid, letter_map):
                dead_count += 1








res = func(m, n, grid)
