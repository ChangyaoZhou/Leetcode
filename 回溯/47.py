def permuteUnique(nums):
    result = []
    path = []
    used = [0] * len(nums)

    def backtracking(nums):
        if len(path) == len(nums):
            #if path not in result:
            result.append(path.copy())
            return

        for i in range(len(nums)):
            if used[i] != 1:
                # 首先，i!=0不是第一项，第一项不会和其他重复
                # nums[i] == nums[i - 1] and used[i - 1] == 0 表示当前数字和前一个数字一样，且前一个数字没用过
                # 在前面的backtracking遍历中，在当前层nums[i]肯定遍历过了，
                # used[i - 1] == 0说明used[i - 1]没有出现在当前层以上的层中,所以此时要跳过取nums[i]的可能性
                # e.g. nums = [1,1,2]
                # 当i=1，第一个数想取第二个1时，第一个数取第一个1的backtracking已经全部完成了，此时要跳过第一个数取第二个1的可能

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == 0:
                    continue

                path.append(nums[i])
                used[i] = 1
                backtracking(nums)
                path.pop()
                used[i] = 0

    # 先将nums排序，这样可以让相同的数互相相邻
    nums.sort()
    backtracking(nums)
    return result


nums = [1,1,2]
nums = [3,3,0,3]
print(permuteUnique(nums))

