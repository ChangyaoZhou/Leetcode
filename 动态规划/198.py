def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    定义 dp 数组用来存储最大的抢劫量，其中 dp[i] 表示如果只有前i个住户时的最大抢劫量。
    由于不能抢劫邻近住户，如果抢劫了第 i -1 个住户，那么就不能再抢劫第 i 个住户，所以
    对于dp中的第i项:
    1 如果偷了这一户，则不能偷i-1户，收益为dp[i-2]+nums[i]
    2 如果没有偷这一户，则收益为dp[i-1]
    取两者最大值，所以
    dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    """
    dp = []
    dp.append(nums[0])
    if len(nums) > 1:
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            max_rob = max(dp[i - 2] + nums[i], dp[i - 1])
            dp.append(max_rob)
    print(dp)
    return dp[-1]

nums = [2, 7, 9, 3, 1]
print(rob(nums))