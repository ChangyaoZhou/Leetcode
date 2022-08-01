def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    示例: 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].
    本题可以用背包算法解决！！！！
    两个子集的元素和相等 = 从原数组中挑出几个元素，使他们的和为sum/2
    【背包问题】
    原数组中的各个数可以看作不同的物品，每个物品的value和weight都是nums中的数值
    从原数组中挑出几个放入背包，背包的最大限重为sum/2(即挑出的几个数的和不大于sum/2)，使背包内的物品价值和(即挑出的几个数的和)最大，
    若背包内的物品价值和为sum/2,则原数组可以分为两个子集，两个子集的元素和相等
    """
    if sum(nums) % 2 == 1:
        return False
    # initialization
    bagsize = int(sum(nums) / 2)
    dp = [[0] * (bagsize + 1) for _ in nums]
    for j in range(bagsize + 1):
        if j >= nums[0]:
            dp[0][j] = nums[0]
        else:
            dp[0][j] = 0
    # recursion
    for i in range(len(nums)):
        for j in range(1, bagsize + 1):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                tmp_value = dp[i - 1][j - nums[i]] + nums[i]
                dp[i][j] = max(dp[i - 1][j], tmp_value)
    return dp[-1][-1] == bagsize

nums = [1,5,11,5, 6, 8, 9, 5]
print(canPartition(nums))

