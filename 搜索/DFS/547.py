def dfs(grid, cur_i, visited):
    for j in range(len(grid)):
        if grid[cur_i][j] == 1 and visited[j] != 1:
            visited[j] = 1
            dfs(grid, j, visited)


def findCircleNum(isConnected):
    """
    创建一个visited数组，用来储存是否访问过每个节点(城市)，
    每次DFS都是为了把彼此有连接的一坨节点(属于同一个省的一坨节点)标为visited，
    依次访问目前没访问过的节点，
    e.g. A--B--C  D  E--F
    首先访问A，并通过DFS将ABC都标为visited，-->province+1
    然后再访问D，将D标为visited,          -->province+1
    然后访问E，并通过DFS将EF都标为visited，-->province+1

    **每次访问一个没访问过的节点，不管他有没有其他节点与之连接，province都会+1!! 因为至少是这个节点自己就可以是一个省

    """
    if len(isConnected) == 0:
        return 0
    city_num = len(isConnected)
    visited = [0] * city_num
    province = 0
    for i in range(city_num):
        if visited[i] != 1:
            dfs(isConnected, i, visited)
            province += 1
    return province


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(isConnected))

