def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    最长连续递增序列，序列中的任何元素不能删除！！！
    定义一个dp列表, dp[i]表示以nums[i]结尾的最长连续递增序列长度
    对于第i个元素，
    - 若其大于前一个元素，则仍未递增，dp[i] = dp[i-1] + 1
    - 若其不大于前一个元素，则以nums[i]结尾的最长连续递增序列需要重新计数，dp[i] = 1
    """
    if len(nums) == 1:
            return len(nums)
    dp = []
    dp.append(1)
    for i in range(1, len(nums)):
        if nums[i] > nums[i -1]:
            dp.append(dp[i-1] + 1)
        else:
            dp.append(1)
    return max(dp)

nums = [1,3,5,4,7]
print(findLengthOfLCIS(nums))



