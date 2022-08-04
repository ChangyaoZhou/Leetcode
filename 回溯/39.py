def combinationSum(candidates, target):
    # 给你一个无重复元素的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target的所有不同组合
    # 各个组合可以是各种长度，且同一个组合内同一个数字可以重复出现，
    # 如果至少一个数字的被选数量不同，则两种组合是不同的。

    result = []
    path = []

    def backtracking(candidates, target, start_idx):
        if sum(path) == target:
            result.append(path.copy())
            return
        if sum(path) > target: # path中的数加和已经大于target，不可能满足path中的数加和为target，则不存入result，退回上一层的下一个backtrack
            return

        for i in range(start_idx, len(candidates)):
            path.append(candidates[i])
            # path中的数加和已经大于target，不可能满足path中的数加和为target，
            # 则不需要进入下一层backtrack，即不需要再在path中加入下一个数字
            if sum(path) <= target:
                backtracking(candidates, target, i)
                # 因为每个组合中可以出现相同的数字，所以backtracking(..., i)而不是backtracking(..., i+1)
                # e.g. candidates = [2,3,5], target = 8, path = [2] 此时在下一层backtrack中path中仍可以添加2
                # 和line13那个条件是一个意思？？但是运行时间会减小20ms
            path.pop()

    backtracking(candidates, target, 0)
    return result


candidates = [2, 5, 3]
target = 8
print(combinationSum(candidates, target))