def maxSubArray(nums):
    '''
    这道题在动态规划里面也出现过，这里我们用贪心算法来解释
    局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
    全局最优：选取最大“连续和”
    局部最优的情况下，并记录最大的“连续和”，可以推出全局最优。
    *** 贪心算法其实类似动态规划，进行比较的是【以每个数结束的连续子序列中的最大和】，在这些最大和中取最大值，即为全局的最大连续子数组和
    '''
    max_sum = -10000
    count = 0
    for num in nums:
        count += num
        if count > max_sum:
            max_sum = count
        if count < 0:
            count = 0
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

