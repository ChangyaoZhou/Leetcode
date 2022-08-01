def largestSumAfterKNegations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    贪心思想: 优先反转负数，如果反转完所有负数，仍然k>0，就将剩余的k次反转全部用于反转绝对值最小的数
    第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
    第二步：从前向后遍历，遇到负数将其变为正数，同时K--
    第三步：如果K还大于0，那么【反复转变】绝对值值最小的元素，将K用完
    第四步：求和
    """
    nums = sorted(nums, key=abs, reverse=True)
    print(nums)
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] *= -1
            k -= 1
            if k == 0:
                break

    if k > 0:
        nums[-1] *= pow(-1, k)
    print(nums)
    return sum(nums)

nums = [2,-3,-1,5,-4]
k = 2
print(largestSumAfterKNegations(nums, k))