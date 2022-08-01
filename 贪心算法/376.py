def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。
    整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
    实际操作上，其实连删除的操作都不用做，因为题目要求的是最长摆动子序列的长度，所以只需要【统计数组的峰值数量】就可以了
    贪心的思想体现在！！！让峰值尽可能的保持峰值，然后删除单一坡度上的节点。
    e.g.
    1->(4)->7->4->(6)->9->2, 删除括号中的数后，仍然保留原有的峰值，删除后的摆动序列长度为5

    """
    pre_diff, cur_diff, count = 0, 0, 1
    for i in range(len(nums) - 1):
        cur_diff = nums[i + 1] - nums[i]
        if cur_diff != 0 and pre_diff * cur_diff <= 0: # 两个数之间差为0，不属于摆动序列
            count += 1
            pre_diff = cur_diff
    return count

nums = [1,7,4,9,2,5]
print(wiggleMaxLength(nums))