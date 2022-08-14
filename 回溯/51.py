def if_valid(path, row, col):
    # 验证棋盘在[row][col]处放棋子是否合法，要满足以下三个条件
    # 不能同行
    # 不能同列
    # 不能同斜线 （45度和135度角）
    n = len(path)
    for i in range(n):
        if path[i][col] == 'Q' or path[row][i] == 'Q':
            return False
    for di, dj in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        i = row
        j = col
        while 0 <= i <= n - 1 and 0 <= j <= n - 1:
            if path[i][j] == 'Q':
                return False
            i += di
            j += dj
    return True

path = [['Q', '.', '.', '.'],
        ['.', '.', '.', 'Q'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.']]
print(if_valid(path, 2, 1))


def solveNQueens(n):
    """
    用回溯来解决，根据皇后的攻击范围，nxn的格子中，每一列只能有一个棋子，同理每一行只能有一个棋子，
    所以可以从第一行开始，在每一行放棋子看成一层backtracking，每一层中遍历在该行的每一列放棋子
    """
    if n == 1:
        return [['Q']]
    result = []
    path = [['.'] * n for _ in range(n)]

    def backtracking(n, path, row):
        if row == n:
            # postprocessing
            final_path = [''.join(subpath)for subpath in path]
            result.append(final_path.copy())
            return

        for col in range(0, n):
            if if_valid(path, row, col):  # 判断在当前的棋子分布path下，能不能把下一个棋子放在（col，row）位置
                path[row][col] = 'Q'
                backtracking(n, path, row + 1)
                path[row][col] = '.'  # 退回上一层backtracking

    backtracking(n, path, 0)
    return result


print(solveNQueens(4))



