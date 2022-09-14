pos = 'tabcaeikjlop'
m = 4
n = 3
commands = ['tab', 'tae', 'akj'] 
print(commands)

pos_map = [[pos[j*n + i]for i in range(n)] for j in range(m)]
pos_map = [['t', 'a', 'b'],
           ['c', 'a', 'e'],
           ['i', 'k', 'j'],
           ['l', 'o', 'p']]
print(pos_map)


def dfs(pos_map, com, i, j, step):
    m = len(pos_map)
    n = len(pos_map[0])
    if i < 0 or i > m-1 or j < 0 or j > n-1 or pos_map[i][j] != com[step] or step > len(com)-1:
        return False
    if step == len(com)-1:
        return com[step] == pos_map[i][j]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nexti = i + di
        nextj = j + dj
        if com[step+1] == pos_map[nexti][nextj]:
            return dfs(pos_map, com, nexti, nextj, step+1)


wrong_command = []
for com in commands:
    valid = False
    for i in range(m):
        if valid:
            break
        for j in range(n):
            if pos_map[i][j] == com[0]:
                if dfs(pos_map, com, i, j, 0):
                    valid = True
                    break
    if not valid:
        wrong_command.append(com)
print(wrong_command)

