def largestDivisibleSubset(nums):
    """
    建立一维dp，dp[i]为以nums[i]为最大值的最大整除子集的size
    e.g. nums = [1, 2, 4, 8, 16]
         dp = [1, 2, 3, 4, 5]
    先将nums从小到大排序
    迭代公式：对于第i个数字，遍历前面的所有数字，
    如果当前数字num[i]可以被前面的数字num[j]整除，则num[j]可以加到num[j]的最大整除子集中，得到的子集仍是整除子集，size是dp[j]+1
    取从0到i-1遍历nums[i],取符合条件的整除子集的最大size，作为dp[i]
    同时存下对应的最大整除子集

    最后，取dp中的最大值，返回对应的最大整除子集
    """

    dp = [1 for _ in range(len(nums))]
    nums.sort()
    dp_divisible_set = [[nums[0]]]

    for i in range(1, len(nums)):
        max_size = 1
        dp_divisible_set.append([nums[i]])
        for j in range(0, i):
            if nums[i] % nums[j] == 0:
                if dp[j]+1 > max_size:
                    max_size = dp[j]+1
                    dp_divisible_set[-1] = dp_divisible_set[j] + [nums[i]]
        dp[i] = max_size
    idx = dp.index(max(dp))
    return dp_divisible_set[idx]


nums = [4,8,10,240]
nums = [2,3,8,9,27]
nums = [5,9,18,54,108,540,90,180,360,720]
print(largestDivisibleSubset(nums))


