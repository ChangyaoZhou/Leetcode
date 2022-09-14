matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]

m = len(matrix)
n = len(matrix[0])


def set_zero(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])
    for p in range(m):
        matrix[p][j] = 0
    for q in range(n):
        matrix[i][q] = 0

#changed = [[0 for _ in range(n)] for _ in range(m)]
#print(changed)
zero_pos = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            zero_pos.append((i, j))
#print(zero_pos)
for i, j in zero_pos:
    set_zero(matrix, i, j)

print(matrix)
for row in matrix:
    for num in row:
        print(num, end='')
    print('')


