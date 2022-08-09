def valid_area(cur_x, cur_y, m, n):
    return 0 <= cur_x < m and 0 <= cur_y < n


def dfs(edge_points, grid, i, j):
    m = len(grid)
    n = len(grid[0])
    # 遍历时超出grid范围，或者发现当前位置已经走过了（grid[i][j] == 2），可以推出当前的dfs
    if not valid_area(i, j, m, n) or grid[i][j] == 2:
        return
    if grid[i][j] == 0:  # 将岛屿边缘的一圈坐标记录下来
        edge_points.add((i, j))
        return

    else:
        # grid[i][j] = 1时，把grid[i][j]置为2
        grid[i][j] = 2
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_i = i + di
        next_j = j + dj
        dfs(edge_points, grid, next_i, next_j)


def shortestBridge(grid):
    """
    可以先找到其中一片岛屿，运用DFS把它标识为2，与另一片岛屿进行区分，也防止重复遍历
    在把第一个岛屿标为2的过程中，收集第一片岛屿附近的海洋（最近一层的海洋0），加入队列queue
    BFS搜索队列，逐层往外“填海造陆”，直到遇到第二片岛屿
    ####一个很直观的图解！！！https://leetcode.cn/problems/shortest-bridge/solution/bfs-tian-hai-zao-lu-ti-jie-si-lu-by-carp-6w8j/

    """
    m = len(grid)
    n = len(grid[0])
    island_found = False
    edge_points = set()
    for i in range(m):
        if island_found:
            break
        for j in range(n):
            if grid[i][j] == 1:
                island_found = True
                dfs(edge_points, grid, i, j)
                break

    # 现在edge_points中存的是和第一个岛屿相邻的一层边缘的坐标
    # 把这一层的0全部填为2，再把外层的0再加入队列，逐层填陆地，直到碰到第二片岛屿
    step = 0
    while edge_points:  # 每一层循环代表从第一个岛屿的边缘向外扩张一步
        step += 1
        new_edge_points = set()
        for ei, ej in edge_points:
            grid[ei][ej] = 2
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_i = ei + di
                next_j = ej + dj
                if valid_area(next_i, next_j, m, n) and grid[next_i][next_j] == 1:
                    # 如果下一步就将触碰到另一个岛屿，则直接返回step
                    return step
                if valid_area(next_i, next_j, m, n) and grid[next_i][next_j] != 2:
                    # 如果下一步没走过(走过的位置都已经标为2)且是海洋(grid[next_i][next_j] = 0)，则把他加入下一层的edge_points
                    new_edge_points.add((next_i, next_j))
        edge_points = new_edge_points  # 当前层的边缘已经全部遍历完了，没有触碰到另一个岛屿，接下来所有边缘点再向外阔一步



A = [[1,1,1,0,0],
     [1,1,1,1,0],
     [0,0,0,0,0],
     [0,0,0,0,0],
     [1,1,1,0,0]]
A = [[0,1,0],
     [0,0,0],
     [0,0,1]]

print(shortestBridge(A))

