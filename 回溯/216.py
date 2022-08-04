def combinationSum3(k, n):
    '''
    找出所有相加之和为 n 的 k 个数, 每个数只能从1到9中取且不重复
    所以，n最大为45=1+2+3+4+5+6+7+8+9
    e.g. n = 18, result =[]

    本题思路类似77组合，因为每个数只能是1到9中的一个，且每个数字只能使用一次，
    所以我们用循环横向遍历从1到9， 用递归进行纵向遍历，当path中已经有k个数字且加和为n时，将path存入result，然后backtrack结束
    '''

    if n > 45:
        return []
    result = []
    path = []

    def backtracking(k, n, start_idx):
        if len(path) == k and sum(path) == n:
            result.append(path.copy())
            return
        if len(path) == k:  # path中已经有了k个数，但是加和不为n，则不存入result，退回上一层的下一个backtrack
            return
        if sum(path) > n:  # path中的数加和已经大于n，不可能满足path中的数加和为n，则不存入result，退回上一层的下一个backtrack
            return

        tmp = k - len(path)
        for i in range(start_idx, min(n, 9) - tmp + 2):  # 如果n<9，则不用从1到9循环，1到n循环即可
            path.append(i)
            backtracking(k, n, i+1)
            path.pop()

    backtracking(k, n, 1)
    # result_sum = [res for res in result if sum(res) == n]
    # 也可以完全按照77题的做法，在1到9中取k个数，返回所有组合，然后只取加和为n的组合
    return result

n = 7
k = 3
print(combinationSum3(k, n))

