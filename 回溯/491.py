def if_increase(nums):
    # 判断一个子序列是否为递增的
    if len(nums) < 2:
        return False
    pre = nums[0]
    for num in nums:
        if pre <= num:
            pre = num
        else:
            return False
    return True

# print(if_increase([4,3]))


def findSubsequences(nums):
    '''
    给一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
    数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
    注意 不是在数组中随意取子集，取出的子序列的顺序一定和原数组中相同！！ 所以不能对数组进行排序！！
    e.g. nums = [4,4,3,2,1] 不能取[3,4], [1,2,3,4], 所以只有一个递增子序列[4,4]
    '''
    result = []
    path = []
    # nums.sort()
    if nums == []:
        return []

    def backtracking(nums, start_idx):
        if start_idx == len(nums):
            return

        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            # 当原数组中有重复的数字，因为我们要找的是递增序列，所以重复指的是子序列完全相同
            # e.g. nums = [4,6,7,7], 如果不去重，将会出现两个完全相同的[4,6,7],
            # 所以只要看result中是否已经有当前的path即可，不用40题的去重方法
            # ps: 40题中需要去掉重复的e.g.[4,7], [7,4]
            if if_increase(path) and not (path in result):
                result.append(path.copy())
            backtracking(nums, i+1)
            path.pop()

    backtracking(nums, 0)
    return result


nums = [4,4,3,2,1]
print(findSubsequences(nums))

