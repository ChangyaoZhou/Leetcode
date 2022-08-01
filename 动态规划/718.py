def findLength(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    *** 本题中对比两个序列时不能删除元素
    dp[i][j] ：以下标i-1为结尾的A，和以下标j-1为结尾的B，最长重复子数组长度为dp[i][j]
               第一行和第一列都初始化为0，实际上没有意义
    A[i - 1]和B[j - 1]相等的时候，dp[i][j] = dp[i - 1][j - 1] + 1
    e.g. nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]，则dp是6x6的列表
    dp:
          3  2  1  4  7
       0  0  0  0  0  0
    1  0  0  0  1  0  0
    2  0  0  1  0  0  0
    3  0  1  0  0  0  0
    2  0  0  2  0  0  0
    1  0  0  0  3  0  0
    另外，最长重复子数组会断开，所以需要用max_len记录目前为止最大的相同序列长度
    """
    dp = [[0] * (len(nums2) + 1) for n in range(len(nums1) + 1)]
    max_len = 0
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
    return max_len

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(findLength(nums1, nums2))
