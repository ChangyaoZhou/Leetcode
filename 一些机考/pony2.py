m = 2
n = 3
grid = [['^', 'v', '<'],
        ['>', '>', '^']]

grid = [['v', 'v', 'v'],
        ['<', '<', '<']]

def dfs(grid, i, j, m, n, visited):
    if i < 0 or j < 0 or i > m-1 or j > n-1 or visited[i][j] == 1:
        return 0
    tmp = 1
    visited[i][j] = 1
    if grid[i][j] == 'v':
        i += 1
    elif grid[i][j] == '<':
        j -= 1
    elif grid[i][j] == '>':
        j += 1
    elif grid[i][j] == '^':
        i -= 1
    tmp += dfs(grid, i, j, m, n, visited)
    return tmp

max_step = 0

for i in range(m):
    for j in range(n):
        visited = [[0 for _ in range(n)] for _ in range(m)]
        num_step = dfs(grid, i, j, m, n, visited)
        max_step = max(max_step, num_step)
print(max_step)