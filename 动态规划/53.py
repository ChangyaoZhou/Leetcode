def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    定义dp数组来表示连续子数组的最大值，dp[i]表示以第i个元素结尾的所有连续子数组的最大和
    e.g. nums = [-2,1,-3,4,-1,2,1,-5,4]
    dp[3] = -2, 所有以-3结尾的连续数组中，元素和最大的[-1, 3],和为2
    对于每一个元素nums[i]，都有两种可能:
    1 和前面连接，以前一个数字结束的连续子数组最大值+当前元素
    2 不和前面连接，从当前元素重新开始
    dp[i]为两种情况结果的较大值。dp[i] = max(dp[i-1] + nums[i], nums[i])
    最后取dp中的最大值即为结果
    """
    if len(nums) < 2:
        return nums[0]
    else:
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))