def valid_board(board, row, col, num):
    n = len(board)
    # 检查同一行，同一列没有相同数字
    for i in range(n):
        if board[row][i] == str(num) or board[i][col] == str(num):
            return False
    square_i = (row // 3) * 3
    square_j = (col // 3) * 3
    # 检查所在九宫格中没有重复的数字
    for i in range(square_i, square_i + 3):
        for j in range(square_j, square_j + 3):
            if board[i][j] == str(num):
                return False
    return True


def solveSudoku(board):
    """
    在本题中，树的纵向backtracking是在每一个位置填入数字，横向遍历是遍历可能的数字1到9
    """

    def backtracking(board):
        n = len(board)

        for row in range(0, n):
            for col in range(0, n):
                if board[row][col] != '.':
                    continue
                for i in range(1, 10):
                    if valid_board(board, row, col, i):  # 判断在当前的board中，能不能在[row, col]处填入数字i
                        board[row][col] = str(i)
                        # 每次进入backtracking，会跳过前面所有给定的，或者已经填入的数字，继续填入下一个数字，然后再进入下一层的backtracking
                        # backtracking如何结束？填入9x9的最后一个数字后，最下层的backtracking返回true，然后每一层都会返回true，从而返回到最上的一层
                        if backtracking(board):
                            return True
                        else:
                            board[row][col] = '.'
                return False
        return True

    backtracking(board)


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(valid_board(board, row=1, col=2, num=3))
solveSudoku(board)
print(board)
