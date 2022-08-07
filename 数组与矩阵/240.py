def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    每次取每一行的最后一个数和target进行比较，
    — 如果target < 当前数，则target不可能在当前行，继续搜索前一行
    - 如果target > 当前数，则target不可能在当前列，继续搜索前一列
    知道找到target或遍历所有行列为止
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while col >= 0 and row < len(matrix):
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False