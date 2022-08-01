def maxUncrossedLines(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    仔细想想 这个题和1143找最大公共子序列是完全一样的！！！
    连线不能相交 = 寻找到两个序列中的公共子序列的相对顺序相同！！！
    两个原序列中的公共子序列有几个元素，就有几条不相交的连线

    """
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
print(maxUncrossedLines(nums1, nums2))