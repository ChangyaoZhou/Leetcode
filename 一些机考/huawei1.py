m = 3
n = 3
t = 10
grid = [[10, 20, 30],
        [20, 70, 40],
        [80, 90, 30]]
m = 4
n = 1
t = 20
#grid = [[10, 20, 30, 50, 70],
        #[160, 140, 120, 100, 80],
        #[170, 180, 190, 200, 210]]
grid = [[90], [80], [60], [45]]


def dfs(i, j, m, n, grid):
    #if i < 0 or i > m-1 or j < 0 or j > n - 1:
        #return 0
    if i == m - 1 and j == n - 1:
        return 1
    step = 1
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_i = i + di
        next_j = j + dj
        if next_i < 0 or next_i > m - 1 or next_j < 0 or next_j > n - 1:
            continue
        if abs(grid[i][j] - grid[next_i][next_j]) > t:
            continue
        if visited[next_i][next_j] == 1:
            continue
        step += dfs(next_i, next_j, m, n, grid)
        return step

# def bfs(i, j, grid):





#i, j = 0, 0
#step = dfs(i, j, m, n, grid)
#visited = [[0 for _ in range(n)] for _ in range(m)]
#print(step)
def is_valid(i, j, grid):
    m = len(grid)
    n = len(grid[0])
    if i < 0 or i > m - 1 or j < 0 or j > n - 1:
        return False
    return True


def func(m, n, grid):
    if m == 1 and n == 1:
        return 0
    '''
    if m == 1:
        for i in range(1, n):
            if abs(grid[0][i] - grid[0][i-1]) > t:
                return -1
        return n - 1
    if n == 1:
        for i in range(1, m):
            if abs(grid[i][0] - grid[i-1][0]) > t:
                return -1
        return m - 1
    '''
    visited = [[0 for _ in range(n)] for _ in range(m)]
    que = [[0, 0]]
    step = 0
    visited[0][0] = 1

    while que:
        #step += 1
        new_que = []
        for i, j in que:
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i = i + di
                next_j = j + dj
                if is_valid(next_i, next_j, grid) and abs(grid[i][j] - grid[next_i][next_j]) <= t \
                        and visited[next_i][next_j] != 1:
                    visited[next_i][next_j] = 1
                    new_que.append([next_i, next_j])
                    if next_i == m-1 and next_j == n-1:
                        return step+1
            step += 1
        que = new_que
    return -1


#visited = [[0 for _ in range(n)] for _ in range(m)]
#print(visited)
print(func(m, n, grid))



