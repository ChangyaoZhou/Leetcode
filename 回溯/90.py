def subsetsWithDup(nums):
    # 给一个整数数组nums，其中可能包含重复元素，请你返回该数组所有可能的子集，【不能包含重复的子集】。
    # 本题可以用和40题一样的方法避免子集的重复！！！
    result = []
    result.append([])
    path = []
    nums.sort()  # 为了方便去重，需要先将nums排序，这样相同的数字会互相相邻

    def backtracking(nums, start_idx):
        if start_idx == len(nums):
            return

        for i in range(start_idx, len(nums)):
            if i > start_idx and nums[i] == nums[i-1]: # 避免重复的操作！！！
                continue
            path.append(nums[i])
            result.append(path.copy())
            backtracking(nums, i+1)
            path.pop()

    backtracking(nums, 0)
    return result


nums = [1,1,2,2]
print(subsetsWithDup(nums))


