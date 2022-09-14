def findNumberOfLIS(nums):
    """
    dp[i]：i之前（包括i）最长递增子序列的长度为dp[i]
    count[i]：以nums[i]为结尾的字符串，最长递增子序列的个数为count[i]
    e.g. [1,3,5,4,7]
    dp[4] = 4, count[i] = 2 ({1, 3, 5, 7}, {1, 3, 4, 7})

    对于dp[i]的更新，和300题一样，
    将第i个元素与其前面的第j个元素进行比较，
    - 若前面有小于第i个元素的，取最长的递增数列长度
    - 若前面没有小于第i个元素的，则dp[i] = 1

    当 nums[i] > nums[j] 时
    区别在于在遍历第j个元素时，
    在nums[i] > nums[j]前提下，如果在[0, i-1]的范围内，找到了j，使得dp[j] + 1 > dp[i]，说明找到了一个更长的递增子序列。
    那么以j为结尾的子串的最长递增子序列的个数，就是最新的以i为结尾的子串的最长递增子序列的个数，即：count[i] = count[j]。

    在nums[i] > nums[j]前提下，如果在[0, i-1]的范围内，找到了j，使得dp[j] + 1 == dp[i]，说明找到了两个相同长度的递增子序列。
    那么以i为结尾的子串的最长递增子序列的个数 就应该加上以j为结尾的子串的最长递增子序列的个数，即：count[i] += count[j];

    最后统计，长度为最大递增子序列长度的子序列一共有多少个（不一定都是以同一个元素结尾的）
    e.g. nums = [2, 2, 2, 2, 2]
         count = [1, 1, 1, 1, 1] dp = [1, 1, 1, 1, 1] result = 5

    """
    dp = [1 for _ in range(len(nums))]
    count = [1 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1, len(nums)):
        max_increasing_len = 1
        for j in range(0, i):
            if nums[i] > nums[j]:
                 if dp[j] + 1 > max_increasing_len:
                     max_increasing_len = dp[j] + 1
                     count[i] = count[j]
                 elif dp[j] + 1 == max_increasing_len:
                     count[i] += count[j]
        dp[i] = max_increasing_len

    print('count', count)
    print('dp', dp)
    result = 0
    for i in range(len(dp)):
        if dp[i] == max(dp):
            result += count[i]
    return result


nums = [1,2,4,3,5,4,7,2]
nums = [2, 2, 2, 3, 3]
print(findNumberOfLIS(nums))
