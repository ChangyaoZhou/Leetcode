def subsets(nums):
    '''
    本题类似于77组合问题，不同在于要把所有中间结果，即树中的所有节点都存到result里面， 就是数组的全部子集
    '''
    result = []
    path = []
    result.append([])

    def backtracking(nums, start_idx):
        if len(path) == len(nums):
            return

        for i in range(start_idx, len(nums)):
            path.append(nums[i])
            result.append(path.copy())
            backtracking(nums, i+1)
            path.pop()

    backtracking(nums, 0)
    return result

nums = [1,2,3]
print(subsets(nums))

