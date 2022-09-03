# 求一个矩阵中最大的二维矩阵（元素和最大）
def get_sub_mat(nums, m, n):
    sub_mat = []
    for i in range(m, m+2):
        sub_mat.extend(nums[i][n:n+2])
    return sub_mat
def find_max2(nums):
    m = len(nums)
    n = len(nums[0])
    if m == 2 and n == 2:
        return nums
    max_val = 0
    max_idx = (0, 0)
    for i in range(0, m-1):
        for j in range(n-1):
            sub_mat = get_sub_mat(nums, i, j)
            sum_val = sum(sub_mat)
            if max_val < sum_val:
                max_val = sum_val
                max_idx = (i, j)
    max_i, max_j = max_idx
    return get_sub_mat(nums, max_i, max_j)
nums = [[0, 0, 0, 0], [0, 2, 3, 0], [0, 5, 7, 0], [0, 0, 0, 100]]
print(find_max2(nums))
