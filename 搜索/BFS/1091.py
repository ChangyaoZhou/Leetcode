def is_valid(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    if i < 0 or i > m-1 or j < 0 or j > n-1:
        return False
    return True


def shortestPathBinaryMatrix(grid):
    m = len(grid)
    n = len(grid[0])
    if grid[0][0] != 0 or grid[-1][-1] != 0:  # 如果左上角起点或右下角终点处不为0，则一定没有符合条件的路线
        return -1
    if m == 1 and n == 1:
        return 1
    que = [(0, 0)]
    count = 1
    grid[0][0] = 2  # 走过的位置标记为2，不用再新建visited来记录走过哪些位置
    #visited = [(0, 0)]

    # 每一次新的一个while循环开始，都是代表走到下一步
    while que:
        new_que = []
        for i, j in que:  #循环当前这一步可能的位置，对于每一个可能的位置扩展出下一步可能的位置
            for di in [0, 1, -1]:
                for dj in [0, 1, -1]:
                    next_i = i + di
                    next_j = j + dj
                    if is_valid(grid, next_i, next_j) and grid[next_i][next_j] == 0:
                        grid[next_i][next_j] = 2
                        #visited.append((next_i, next_j))
                        new_que.append((next_i, next_j))
                    if next_i == m-1 and next_j == n-1:
                        return count+1
        count += 1
        que = new_que
    return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,0,0],
        [1,1,0],
        [1,1,1]]
#grid = [[0,1],[1,0]]
print(shortestPathBinaryMatrix(grid))
