n = 8
k = 4
grid = [[0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 4, 4, 0, 0, 0],
        [1, 0, 0, 4, 0, 0, 0, 0],
        [1, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 4, 4, 0, 2, 2, 0],
        [0, 0, 0, 4, 0, 0, 2, 0],
        [0, 0, 0, 4, 4, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
command = [['1', 'L'], ['2', 'D'], ['3', 'R'], ['1', 'U']]


def dfs(edge_points, grid, i, j, num):
    n = len(grid)
    if i < 0 or i > n-1 or j < 0 or j > n-1 or grid[i][j] != num or (i, j) in edge_points:
        return

    edge_points.add((i, j))
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_i = i + di
        next_j = j + dj
        dfs(edge_points, grid, next_i, next_j, num)


command_dict = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
for num_move, comm in command:
    num = int(num_move)
    num_found = False
    if_conflict = False
    num_points = set()
    for i in range(n):
        if num_found:
            break
        for j in range(n):
            if grid[i][j] == num:
                num_found = True
                dfs(num_points, grid, i, j, num)
                break
    if num_points != set():
        new_num_points = set()
        di, dj = command_dict[comm]
        for i, j in num_points:
            next_i = i + di
            next_j = j + dj
            if next_i < 0 or next_i > n-1 or next_j < 0 or next_j > n-1 or (grid[next_i][next_j] != 0 and grid[next_i][next_j] != num):
                if_conflict = True
                break
            new_num_points.add((next_i, next_j))
        if not if_conflict:
            for i, j in num_points:
                grid[i][j] = 0
            for i, j in new_num_points:
                grid[i][j] = num
#print(grid)
for line in grid:
    line_str = [str(x) for x in line]
    print(''.join(line_str))

