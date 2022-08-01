def rob_sub(nums):
    dp = []
    dp.append(nums[0])
    if len(nums) > 1:
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            max_rob = max(dp[i - 2] + nums[i], dp[i - 1])
            dp.append(max_rob)
    return dp[-1]


def rob_cycle(nums):
    """
    :type nums: List[int]
    :rtype: int
    213和198的区别在于，第一件房和最后一间房不能同时被偷
    如何才能保证第一间房屋和最后一间房屋不同时偷窃呢？
    如果偷窃了第一间房屋，则不能偷窃最后一间房屋，因此偷窃房屋的范围是第一间房屋到最后第二间房屋；
    如果偷窃了最后一间房屋，则不能偷窃第一间房屋，因此偷窃房屋的范围是第二间房屋到最后一间房屋。
    所有情况都包含在以上两种情况里面！！！(偷1不偷n，偷n不偷1，1和n都不偷)
    因此取两种情况的最大值即可 max(rob_sub(nums[1:]), rob_sub(nums[:-1]))
    rob_sub 部分和198解法相同，


    """
    if len(nums) < 3:
        return rob_sub(nums)
    else:
        return max(rob_sub(nums[1:]), rob_sub(nums[:-1]))

nums = [2, 7, 9, 3, 1]
print(rob_cycle(nums))