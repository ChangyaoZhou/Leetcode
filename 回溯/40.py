def combinationSum2(candidates, target):
    # 给定一个数组 candidates 和一个目标数 target ，candidates中可能存在重复的元素
    # 找出 candidates 中所有可以使数字和为 target 的组合。
    # # 各个组合可以是各种长度, 但是candidates 中的每个数字在每个组合中只能使用一次。
    # initialization
    result = []
    path = []
    candidates.sort()  # 排序为了后面去重方便！！

    def backtracking(candidates, target, start_idx):
        if sum(path) == target:
            result.append(path.copy())
            return
        if sum(path) > target:
            return

        for i in range(start_idx, len(candidates)):
            # e.g. candidates = [10,1,2,7,6,1,5], 经过排序后[1,1,2,5,6,7,10],相等的数字肯定是相邻的
            # 首先在第一层 i=0时，path = [candidates[0], ...] = [1, ...]
            # 然后在循环第一层, i=1时，因为candidates[1] == candidates[0]，此时当前的candidates[1]不是第一个数且和前一位重复了
            # 需要直接跳过path = [candidates[1], ...] = [1, ...]
            if i > start_idx and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtracking(candidates, target, i + 1)
            path.pop()

    backtracking(candidates, target, 0)
    return result


candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))



