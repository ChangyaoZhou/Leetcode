def dfs(board, curi, curj):
    if curi < 0 or curj < 0 or curi == len(board) or curj == len(board[0]) or board[curi][curj] != 'O':
        # 如果搜索走出了board的范围，或者不再是O了，就停止
        return
    board[curi][curj] = 'T'
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_i = curi + di
        next_j = curj + dj
        dfs(board, next_i, next_j)


def solve(board) -> None:
    """
    任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
    搜索所有的边界，所有和边界相连的格子(能通过上下左右移动到达的)里面的O，都不变，除此之外，其他被X包围的O，全部换为X
    方法: 首先遍历所有的边界，将所有和边界相连的O换为T，这些O是不需要变成X的
         然后把board中剩余的O(被X包围的O)换为X
         最后将所有的T再换回O
    """
    m = len(board)
    n = len(board[0])

    for i in range(m):
        dfs(board, i, 0)
        dfs(board, i, n-1)
    for j in range(n):
        dfs(board, 0, j)
        dfs(board, m-1, j)
    print(board)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'T':
                board[i][j] = 'O'




board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
solve(board)
print(board)

