def twoSum(nums, target):
    '''basic solution 暴力循环解法
    sol = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                sol.append(i)
                sol.append(j)
    return sol
    法二: 双指针
    先将nums排序，idx_sorted中存了排序后的nums的每一项对应的索引
    e.g. nums = [3,2,4]
    nums_dix_sorted = [(3,0), (2,1), (4,2)]储存了nums中对应的数值和索引
    排序后 nums_dix_sorted = [(2,1), (3,0), (4,2)], idx_sorted = [1,0,2]
    利用双指针找出正确的nums后，从idx_sorted中提取原来的索引
    '''
    nums_idx = [(nums[i], i) for i in range(len(nums))]
    nums_idx_sorted = sorted(nums_idx)
    idx_sorted = [nums_idx_sorted[i][1] for i in range(len(nums))]
    sum_num = target - 1
    i = 0
    j = len(nums) - 1
    while (True):
        if nums_idx_sorted[i][0] + nums_idx_sorted[j][0] < target:
            i += 1
        elif nums_idx_sorted[i][0] + nums_idx_sorted[j][0] > target:
            j -= 1
        elif nums_idx_sorted[i][0] + nums_idx_sorted[j][0] == target:
            return [idx_sorted[i], idx_sorted[j]]


nums = [3,2,4]
target = 6
print(twoSum(nums, target))


