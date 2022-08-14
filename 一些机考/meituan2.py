m, n, k = 2, 2, 5
commands = 'SWSWS'
command_list = list(commands)

board = [[0] * n for i in range(m)]
board[0][0] = 1
# print(board)

def if_clean(board):
    m = len(board)
    n = len(board[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                return False
    return True

i = 0
j = 0
com_dict = {'S': (1, 0), 'D': (0, 1), 'W': (-1, 0), 'A':(0, -1)}
for m in range(len(command_list)):
    di, dj = com_dict[command_list[m]]
    i += di
    j += dj
    board[i][j] = 1
    if if_clean(board):
        print('Yes')
        print(m+1)
        break
if not if_clean(board):
    m = len(board)
    n = len(board[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                count += 1
    print('No')
    print(count)





