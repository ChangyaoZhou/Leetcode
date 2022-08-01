def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    *** 最长递增 子序列注意本题中原序列中的元素可随意删除！！！
    动态规划的五个步骤
    1 【定义dp】: dp[i]表示以nums[i]结尾的最长递增子序列的长度
    2 【递归方程】: if (nums[i] > nums[j]), dp[i] = max(dp[i], dp[j] + 1)
    3 【dp初始化】: dp[0] = 1
    4 【遍历顺序】: 遍历i的循环在外层，遍历j则在内层
    首先遍历所有的元素，对于第i个元素，内部遍历其前面的所有元素，
    将第i个元素与其前面的第j个元素进行比较，
    - 若前面有小于第i个元素的，取最长的递增数列长度
    - 若前面没有小于第i个元素的，则dp[i] = 1
    """
    if len(nums) == 1:
        return len(nums)
    dp = []
    dp.append(1)
    for i in range(1, len(nums)):
        seq_len = []
        for j in range(i):
            if nums[i] > nums[j]:
                seq_len.append(dp[j] + 1)
            elif j == i -1:
                seq_len.append(1)
        dp.append(max(seq_len))
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
nums = [0]
print(lengthOfLIS(nums))