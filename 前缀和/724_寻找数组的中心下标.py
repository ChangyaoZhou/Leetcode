def pivotIndex(nums):
    # 暴力解法,用时比较长
    '''
    if sum(nums[1:]) == 0:
        return 0
    for i in range(1, len(nums)-1):
        if sum(nums[0: i]) == sum(nums[i+1:]):
            return i
    if sum(nums[:-1]) == 0:
        return len(nums)-1
    return -1
    '''
    #前缀和1
    #对于第i个元素，他前面元素的加和 如果等于 （所有元素加和减去当前元素）的一半，则找到了中心坐标
    '''
    num_sum = sum(nums)
    curr_sum = 0
    for i in range(len(nums)):
        if curr_sum == (num_sum - nums[i]) * 0.5:
            return i
        curr_sum += nums[i]
    return -1
    '''
    #前缀和2 用时最短！！
    #若左侧元素和等于右侧元素和，返回中心下标 i
    sum_left, sum_right = 0, sum(nums)
    for i in range(len(nums)):
        sum_right -= nums[i]

        if sum_left == sum_right:
            return i
        sum_left += nums[i]
    return -1



nums = [1, 7, 3, 6, 5, 6]
print(pivotIndex(nums))

