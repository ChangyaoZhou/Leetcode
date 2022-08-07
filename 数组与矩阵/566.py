def matrixReshape(mat, r, c):
    """
    如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵
    依次将原数组中的数字放入reshape数组，放满一行后放入mat_reshape
    """
    n = len(mat)
    m = len(mat[0])
    if n * m != r * c:  # illegal
        return mat

    mat_reshape, new_row = [], []
    for row in mat:
        for num in row:
            new_row.append(num)
            if len(new_row) == c:
                mat_reshape.append(new_row)
                new_row = []
    return mat_reshape


mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(matrixReshape(mat, r, c))

