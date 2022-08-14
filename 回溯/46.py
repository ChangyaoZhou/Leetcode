def permute(nums):
    """
    因为本题中要求的是一个数组的全排列可能，首先排列是有序的，也就是说 [1,2] 和 [2,1] 是两个集合，这和之前分析的子集以及组合所不同的地方。
    所以不再需要start_idx来控制不能取之前的数字，但是需要一个used数组，标记已经选择的元素
    """
    result = []
    path = []
    used = [0] * len(nums)

    def backtracking(nums):
        # backtracking结束条件：path到达一定长度
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(0, len(nums)):
            # 用used保证不会取到重复的数字
            if used[i] == 1:
                continue
            else:
                path.append(nums[i])
                used[i] = 1
                backtracking(nums)
                # 返回上一步，used也要恢复到上一层的状态
                path.pop()
                used[i] = 0

    backtracking(nums)
    return result


nums = [1, 2, 3]
print(permute(nums))

