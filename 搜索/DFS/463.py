def valid_area(cur_x, cur_y, m, n):
    return 0 <= cur_x < m and 0 <= cur_y < n


def islandPerimeter(grid):
    # 简单的思路：岛屿的周长就是岛屿方格和非岛屿方格相邻的边的数量。*****
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):
        if not valid_area(i, j, m, n):
            # 从一个岛屿方格走向网格边界，周长加 1
            return 1
        if grid[i][j] == 0:
            # 从一个岛屿方格走向水域方格，周长加 1
            return 1
        if grid[i][j] == 2:
            # 走到了之前访问过的格子，周长不变
            return 0
        grid[i][j] = 2  # 将已经访问过的格子标记为2
        border = 0
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_i = i + di
            next_j = j + dj
            border += dfs(next_i, next_j)
        return border

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return dfs(i, j)

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

print(islandPerimeter(grid))


"""
对于一个有参数的函数，eg，add，不能使用他范围之外的变量，无法把变量d设置为全局变量，即在add函数内不能调用d，除非把d加入add的参数
但是如果d是一个列表，就可以在add函数内不能调用和改变d
"""

def test(a):
    d = 0
    def add(a):
        global d
        #if a == 9:
            #return
        a+= 2
        d+=3
        #add(a, d)
        #print(d)

    add(a)
    print(d)


#test(a=3)
